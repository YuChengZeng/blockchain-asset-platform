# -*- coding: utf-8 -*-
import re
from hashlib import sha1
import time
from datetime import datetime
from collections import Counter
from flask import Flask, session, g, render_template, request, redirect, url_for, abort, flash, Response
from flask_openid import OpenID
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS
from flask_socketio import SocketIO
from sqlalchemy.exc import SQLAlchemyError
from web3 import Web3
from web3.auto import w3
from werkzeug.utils import secure_filename
from eth_account.messages import encode_defunct
from sqlalchemy.orm import sessionmaker
from jinja2 import evalcontextfilter, Markup, escape
from solid.extension import db
from solid.views.misc import items_pagebar, last_page
from solid.views.config import *  # if for PyCharm execution, use script.config
from solid.models.users import Users
from solid.models.user import User
from solid.models.pi_user import Pi_user
from solid.models.asset_detail import Asset_detail
from solid.models.asset_nft import Asset_nft
from solid.models.launch_to_nft import Launch_to_nft
from solid.models.application_list import Application_list
from solid.models.ticket import Ticket
from solid.models.room_list import Room_list
from solid.models.set_room import Set_room

app = Flask(__name__)
app.secret_key = 'sdgDDghWBgseth41WEFD,rst4G1rCCHSk6xf8g4gpTokjdsfheEE2121htRR'
app.config.from_object('websiteconfig')  # 從 websiteconfig.py 讀取設定
app.config['TEMPLATES_AUTO_RELOAD'] = True  # 每次 request 刷新 html
CORS(app, resources={r"/*":{"origins":"*"}})
socketio = SocketIO(app, cors_allowed_origins='*')

oid = OpenID(app, '/tmp/flask_openid')  # session與登入檢查用
db.init_app(app) # 在 app 物件建立後
DebugToolbarExtension(app)
_paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')  # for nl2br


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.before_request
def load_current_user():
    print(request.path)
    if request.path[:8] == '/static/' or request.path == url_for('login'):
        # 靜態檔案存取, need not check if login or not.
        pass
    elif 'api' in request.path:
        pass
    elif 'account' not in session:  # 使用者沒有登入的情況, 導回登入頁
        # need to login now, redirect to login page
        return redirect(url_for('login'))


@app.route('/')
def show_entries():
    """導入頁
    :return: None
    """
    if 'currentAccount' in session:
        print(f'Show Entries')
        print(session['currentAccount'])

        query = db.session.query(Application_list) \
            .join(Launch_to_nft, Launch_to_nft.launch_id == Application_list.launchId) \
            .join(Asset_nft, Asset_nft.NftId == Launch_to_nft.tokenId) \
            .join(Asset_detail, Asset_detail.transactionHash == Asset_nft.transactionHash) \
            .add_columns(Launch_to_nft.tokenId, Asset_detail.title, Asset_detail.creator, Asset_detail.description,
                         Asset_detail.subject, Asset_detail.transactionHash)
        application_list = query.all()
        application_list = [sublist[1:] for sublist in application_list]
        application_list = Counter(application_list)
        # print(application_list)
        commodities_rank = []
        for key, value in application_list.items():
            commodities_rank.append([key[0], key[1], key[2], key[3], key[4], key[5], value])

        # print(commodities_rank)

        query = db.session.query(Ticket) \
            .join(Room_list, Ticket.room_id == Room_list.room_id) \
            .add_columns(Ticket.room_id, Room_list.title, Room_list.introduction)
        ticket_list = query.all()
        ticket_list = [sublist[1:] for sublist in ticket_list]
        ticket_list = Counter(ticket_list)
        # print(ticket_list)
        ticket_rank = []
        for key, value in ticket_list.items():
            ticket_rank.append([key[0], key[1], key[2], value])

        # print(ticket_rank)
        return render_template('default.html', address_CT=address_CT, CT_abi=CT_abi_json, commodities_rank=commodities_rank, ticket_rank=ticket_rank)
    else:
        flash('not a user')
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """登入執行, 或顯示登入頁
    """
    if request.method == 'POST' and request.form['account'] != '':
        currentAccount = request.form['address']
        account = request.form['account']
        nickname = request.form['nickname']
        target_user = Pi_user.query.filter_by(account=account).first()
        session['currentAccount'] = currentAccount
        session['account'] = account
        session['nickname'] = nickname
        session['_id'] = target_user._id
        session['auth_token'] = target_user.token
        if 'cart' not in session:
            session['cart'] = []
        flash('You have logged in.')
        # 將使用者錢包地址和PI帳號綁定
        target_user.address = currentAccount
        db.session.commit()
        return redirect(url_for('show_entries'))
    elif request.method == 'POST' and request.form['account'] == '':
        return render_template('pi_iframe.html')
    elif 'token' not in request.cookies:
        return render_template('pi_iframe.html')
    else:
        token = request.cookies.get('token')
        user = Pi_user.query.filter_by(token=token).first()
        return render_template('login.html', user=user)


@app.route('/api_PI_login', methods=['GET', 'POST'])
def api_PI_login():
    print(f'login_data')
    login_data = request.get_json(force=True)
    print(f'--------------------------')
    print(f'{login_data}')
    print(f'--------------------------')

    # 登入後更新來自PI的新token
    target_user = Pi_user.query.filter_by(account=login_data['user']['account']).first()
    target_user.token = login_data['token']
    target_user._id = login_data['user']['_id']
    target_user.email = login_data['user']['email']
    db.session.commit()
    print(f'User Info Finish Update')

    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('account', None)
    session.pop('nickname', None)
    session.pop('currentAccount', None)
    session.pop('auth_token', None)
    session.pop('_id', None)
    resp = Response("Cookie deleted!")
    resp.set_cookie('session', '', expires=0)

    flash('You have logged out.')
    return redirect(url_for('login'))


@app.route('/api_signin_param', methods=['GET', 'POST'])
def api_signin_param():
    print(f'signin_param')
    signin_param = request.get_json(force=True)
    print(f'--------------------------')
    print(f'{signin_param}')
    print(f'--------------------------')

    data = Pi_user(
        nickname=signin_param['nickname'],
        account=signin_param['account'],
        password=signin_param['password'],
        token=signin_param['token']
    )
    db.session.add(data)
    db.session.commit()
    print(f'User Created')

    return signin_param


@app.route('/test')
def test():
    print(f'Test')
    return render_template('test.html')


@app.template_filter('strftime')
def _jinja2_filter_datetime(date, fmt=None):
    if fmt:
        return date.strftime(fmt)
    else:
        return date.strftime('%Y-%m-%d %H:%M:%S')


from solid.views import object_data
from solid.views import web3
from solid.views import asset
from solid.views import curation
from solid.views import visitor
from solid.views import filter

app.register_blueprint(object_data.mod, url_prefix='/object_data')
app.register_blueprint(web3.mod, url_prefix='/web3')
app.register_blueprint(asset.mod, url_prefix='/asset')
app.register_blueprint(curation.mod, url_prefix='/curation')
app.register_blueprint(visitor.mod, url_prefix='/visitor')
app.register_blueprint(filter.mod, url_prefix='/filter')


if __name__ == '__main__':
    app.run()
