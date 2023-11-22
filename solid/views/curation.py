# -*- coding: utf-8 -*-
from datetime import datetime
import os
import requests
from eth_account.messages import encode_defunct
from flask import Blueprint, render_template, jsonify, redirect, url_for, request, g, session, flash, Flask
from flask_cors import cross_origin
from flask_cors import CORS
import time
from re import escape
from sqlalchemy.exc import SQLAlchemyError
from solid.extension import db
from solid.views.config import *  # if for PyCharm execution, use script.config
from solid.views.filter import source
from solid.models.asset_detail import Asset_detail
from solid.models.asset_nft import Asset_nft
from solid.models.launch_to_nft import Launch_to_nft
from solid.models.set_room import Set_room
import json
from web3 import Web3
from web3.auto import w3
from web3.middleware import geth_poa_middleware
from web3.exceptions import TransactionNotFound
from werkzeug.utils import secure_filename
from omeka_s_tools.api import OmekaAPIClient

mod = Blueprint('curation', __name__)
CORS(mod)


def get_launch_detail_list():
	# 讀取合約中所有Launch事件
	to_block = chain.eth.blockNumber
	launch_detail_list = []
	event_filter = contract_ART.events['Launch'].createFilter(fromBlock=0, toBlock=to_block)
	for event in event_filter.get_all_entries():
		# 針對每個Launch事件檢查其launch_detail的status
		launch_detail = contract_ART.functions.launchDetail(event['args']['launchId']).call()
		if launch_detail[4]:
			# 若為真就加入list中
			launch_detail.append(event['args']['launchId'])
			launch_detail_list.append(launch_detail)
	print(f'{len(launch_detail_list)} Launch Detail {launch_detail_list}')
	return launch_detail_list


def repalce_detail(launch_detail_list, asset_list):
	asset_list = [sublist[1:] for sublist in asset_list]
	launch_detail_list = [item for item in launch_detail_list if item[0] in [b[0] for b in asset_list]]
	asset_dict = {}
	for asset in asset_list:
		asset_dict[asset[0]] = asset[1], asset[2], asset[3]
	# print(f'{launch_detail_list}')
	# 遍歷每個 list，進行替換
	for launch_detail in launch_detail_list:
		value = asset_dict[launch_detail[0]]
		launch_detail.append(value[0])
		launch_detail.append(value[1])
		launch_detail.append(value[2])
	return launch_detail_list


def search_core():  # 加入搜尋條件的商品列表
	if request.method == 'POST' and request.form['s_key'] and request.form['s_value']:
		session['s_key'] = request.form['s_key']
		session['s_value'] = request.form['s_value']

	if session['s_value'] == '':
		redirect(url_for('curation.commodities'))

	search_target = getattr(Asset_detail, session['s_key'])

	launch_detail_list = get_launch_detail_list()

	query = db.session.query(Asset_nft) \
		.join(Asset_detail, Asset_nft.transactionHash == Asset_detail.transactionHash) \
		.join(Launch_to_nft, Asset_nft.NftId == Launch_to_nft.tokenId) \
		.add_columns(Asset_nft.NftId, Asset_detail.title, Asset_detail.transactionHash, Asset_nft.source) \
		.filter(search_target.like('%' + session['s_value'] + '%'))
	# print(query)

	asset_list = query.all()
	# print(asset_list)
	launch_details = repalce_detail(launch_detail_list, asset_list)
	session['s_value'] = ''
	return launch_details


@mod.route('/commodities', methods=['GET', 'POST'])
def commodities():  # 商品列表
	launch_detail_list = get_launch_detail_list()

	query = db.session.query(Asset_nft) \
		.join(Asset_detail, Asset_nft.transactionHash == Asset_detail.transactionHash) \
		.join(Launch_to_nft, Asset_nft.NftId == Launch_to_nft.tokenId) \
		.add_columns(Asset_nft.NftId, Asset_detail.title, Asset_detail.transactionHash, Asset_nft.source)
	asset_list = query.all()
	# print(asset_list)

	launch_details = repalce_detail(launch_detail_list, asset_list)
	# print(f'{launch_details}')

	return render_template('web3/commodities.html', launch_detail_list=launch_details, address_ART=address_ART, address_CT=address_CT, ART_abi=ART_abi_json, CT_abi=CT_abi_json)


@mod.route('/search', methods=['GET', 'POST'])
def search():  # 加入搜尋條件的商品列表
	launch_details = search_core()
	return render_template('web3/commodities.html', launch_detail_list=launch_details, address_ART=address_ART,
						   address_CT=address_CT, ART_abi=ART_abi_json, CT_abi=CT_abi_json)


@mod.route('/commodities_view/<launch_id>/<day>', methods=['GET', 'POST'])
def commodities_view(launch_id, day):
	# target = Asset_detail.query.filter_by(transactionHash=transactionHash) \
	# 	.join(Asset_nft, Asset_detail.transactionHash == Asset_nft.transactionHash) \
	# 	.add_columns(Asset_detail.title, Asset_detail.creator, Asset_detail.description, Asset_detail.subject, Asset_nft.source) \
	# 	.first()

	# launch_detail_list = get_launch_detail_list()
	# for sublist in launch_detail_list:
	# 	print(sublist)
	# 	print(launch_id)
	# 	print(sublist[5])
	# 	if sublist[5] == launch_id:
	# 		day = sublist[1]
	# 		print(str(day))

	target = Launch_to_nft.query.filter_by(launch_id=launch_id) \
		.join(Asset_nft, Launch_to_nft.tokenId == Asset_nft.NftId) \
		.join(Asset_detail, Asset_detail.transactionHash == Asset_nft.transactionHash) \
		.add_columns(Asset_detail.title, Asset_detail.creator, Asset_detail.description, Asset_detail.subject, Asset_nft.source, Launch_to_nft.price, Launch_to_nft.launch_id) \
		.first()
	# print(f'---{target.title}')

	return render_template('web3/commodities_view.html', target=target, address_ART=address_ART, address_CT=address_CT,
						   ART_abi=ART_abi_json, CT_abi=CT_abi_json, day=day)


@mod.route('/license', methods=['GET', 'POST'])
def license():
	to_block = chain.eth.blockNumber

	license_list = []
	# fetch Application event
	event_filter = contract_ART.events['Application'].createFilter(fromBlock=0, toBlock=to_block)
	for event in event_filter.get_all_entries():
		# 過濾錢包擁有者的event
		if event['args']['operator'] == session['currentAccount']:
			license_list.append(event['args']['licenseId'])
	# print(f'Users all license {license_list}')
	license_detail_list = []
	for license in license_list:
		license_detail = contract_ART.functions.licenseDetail(license).call()
		print(f'License EXP {license_detail[1]} Now {time.time()}')
		if license_detail[1] >= time.time():
			struct_time = time.localtime(license_detail[1])
			exp_date = time.strftime("%Y/%m/%d %H:%M:%S", struct_time)
			license_detail[1] = exp_date
			license_detail_list.append(license_detail)
	# print(f'License Detail List {license_detail_list}')

	asset_list = db.session.query(Asset_nft) \
		.join(Asset_detail, Asset_nft.transactionHash == Asset_detail.transactionHash) \
		.join(Launch_to_nft, Asset_nft.NftId == Launch_to_nft.tokenId) \
		.add_columns(Asset_nft.NftId, Asset_detail.title, Asset_detail.subject, Asset_detail.transactionHash,
					 Asset_nft.source) \
		.all()
	# print(asset_list)
	asset_list = [sublist[1:] for sublist in asset_list]

	for asset in asset_list:
		list(asset)
		# print(f'{asset}')
	asset_dict = {}
	for asset in asset_list:
		asset_dict[asset[0]] = asset[1], asset[3], asset[4]
	# print(f'Asset Dict{asset_dict}')
	# 遍歷每個 list，進行替換
	for license_detail in license_detail_list:
		title = asset_dict[license_detail[0]][0]
		license_detail.append(asset_dict[license_detail[0]][2])
		license_detail[0] = title
	# print(f'{license_detail_list}')
	sorted_license_detail = sorted(license_detail_list, key=lambda x: x[0])
	if request.method == 'POST' and request.form['s_key']:
		sorted_license_detail = sorted(license_detail_list, key=lambda x: x[1])

	return render_template('web3/license.html', license_detail_list=sorted_license_detail)


@mod.route('/show_room', methods=['GET', 'POST'])
def show_room():
	# 展間列表
	url = 'https://dev-partyisland.dlll.nccu.edu.tw/api/seller/{}/exhibitions'.format(session['_id'])
	headers = {"Authorization": "Bearer {}".format(session['auth_token'])}
	response = requests.get(url, headers=headers)
	my_rooms = json.loads(response.text)

	if my_rooms['status'] == 403:
		print(f'You Have To Be A Blocker')
		return redirect(url_for('show_entries'))
	print(f'my_rooms {my_rooms}')
	print('--------------------------------')
	rooms = my_rooms['data']
	for room in rooms:
		# print(room['_id'])
		room_data = db.session.query(Set_room).filter(Set_room.room_id == room['_id']).first()
		print(room_data)
		if room_data is None:
			# 如果 room_data 為 None，表示資料庫中沒有該筆資料，進行新增操作
			new_room = Set_room(
				address='0x',
				room_id=room['_id'],
				price='0',
				blockNumber='0'
			)
			db.session.add(new_room)
			db.session.commit()
		else:
			room_data = db.session.query(Set_room) \
				.filter(Set_room.room_id.like(room['_id'])) \
				.order_by(Set_room.id.desc()) \
				.first()
			room['price'] = room_data.price
	print(f'Room Data {rooms}')

	return render_template('web3/show_room.html', rooms=rooms, address_TT=address_TT, address_CT=address_CT,
						   TT_abi=TT_abi_json, CT_abi=CT_abi_json)
