# -*- coding: utf-8 -*-
from copy import deepcopy
from datetime import datetime
import os
from eth_account.messages import encode_defunct
from flask import Blueprint, render_template, jsonify, redirect, url_for, request, g, session, flash, Flask
from flask_cors import cross_origin
from flask_cors import CORS
import time
from re import escape
from sqlalchemy.exc import SQLAlchemyError
from solid.extension import db
from solid.views.misc import items_pagebar, last_page
from solid.views.config import *  # if for PyCharm execution, use script.config
from solid.views.filter import source
from solid.models.token import Token
from solid.models.asset_detail import Asset_detail
from solid.models.asset_nft import Asset_nft
from solid.models.launch_to_nft import Launch_to_nft
import json
from web3 import Web3
from web3.auto import w3
from web3.middleware import geth_poa_middleware
from web3.exceptions import TransactionNotFound
from solid.models.user import User
from werkzeug.utils import secure_filename
from omeka_s_tools.api import OmekaAPIClient


mod = Blueprint('asset', __name__)
CORS(mod)


def repalce_detail(asset_detail_list, asset_list):
	asset_list = [sublist[1:] for sublist in asset_list]
	asset_dict = {}
	for asset in asset_list:
		asset_dict[asset[0]] = asset[1], asset[2], asset[3]
	# print(asset_dict)
	# 遍歷每個 list，進行替換
	for asset_detail in asset_detail_list:
		# print(asset_detail)
		value = asset_dict[asset_detail[0]]
		asset_detail.append(value[0])
		asset_detail.append(value[1])
		asset_detail.append(value[2])
	# print(f'repalce_detail{asset_detail_list}')
	return asset_detail_list


def search_core():  # 加入搜尋條件的搜尋
	asset_detail = []
	asset_detail_list = []
	my_address = session['currentAccount']
	if request.method == 'POST' and request.form['s_key'] and request.form['s_value']:
		session['s_key'] = request.form['s_key']
		session['s_value'] = request.form['s_value']

	if session['s_value'] == '':
		redirect(url_for('asset.asset_list'))

	search_target = getattr(Asset_detail, session['s_key'])

	# launch_detail_list = get_launch_detail_list()
	query = db.session.query(Asset_nft) \
		.join(Asset_detail, Asset_nft.transactionHash == Asset_detail.transactionHash) \
		.add_columns(Asset_nft.NftId, Asset_detail.title, Asset_detail.subject, Asset_nft.operator, Asset_nft.transactionHash, Asset_nft.img) \
		.filter(Asset_nft.operator.like(my_address)) \
		.filter(search_target.like('%' + session['s_value'] + '%'))

	asset_list = query.all()

	for asset in asset_list:
		# print(f'{asset}')
		asset_detail.append(asset.NftId)
		asset_detail.append(asset.title)
		asset_detail.append(asset.subject)
		asset_detail.append(asset.operator)
		asset_detail.append(asset.transactionHash)
		asset_detail.append(asset.img)
		asset_detail_list.append(asset_detail)
		asset_detail = []

	# print(f'{asset_detail_list}')
	session['s_value'] = ''
	return asset_detail_list


@mod.route('/upload', methods=['GET', 'POST'])
def upload():
	# 上傳位址、類型、大小
	UPLOAD_FOLDER = '/root/test_upload/'
	ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])
	MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
	creator = session['nickname']

	if request.method == 'POST':
		# 上傳檔案到網站伺服器
		file = request.files['load_file']
		filename = secure_filename(file.filename)
		file.save(os.path.join(UPLOAD_FOLDER, filename))

		# 上傳檔案和metadata到omekas伺服器
		omeka_auth = OmekaAPIClient(
			api_url='http://localhost:81/api',
			key_identity='C1qUawykxTyB61j1rf0DPwJw68z0RgZo',
			key_credential='SZtaDwSzUR357zI5z0qKW9S5cU9dSw96'
		)
		items = omeka_auth.get_resources('items')
		# print(items['total_results'])
		print(len(items['results']))

		# 取得網頁中填入資料
		title = request.form.get('title')
		creator = request.form.get('creator')
		description = request.form.get('description')
		subject = request.form.get('subject')
		transactionHash = request.form.get('tx_hash')
		item = {
			'dcterms:title': [
				{
					'value': title
				}
			],
			'dcterms:creator': [
				{
					'value': creator
				}
			],
			'dcterms:description': [
				{
					'value': description
				}
			],
			'dcterms:subject': [
				{
					'value': subject
				}
			],
			'dcterms:source': [
				{
					'value': transactionHash
				}
			]
		}
		payload = omeka_auth.prepare_item_payload(item)
		# print(payload)
		payload_with_media = omeka_auth.add_media_to_payload(payload, media_files=['/root/test_upload/' + filename])
		assert json.loads(payload_with_media['data'][1])
		new_item = omeka_auth.add_item(payload, media_files=['/root/test_upload/' + filename])
		# print(new_item)

		# 上傳metadata到資料庫
		detail = Asset_detail(
			title=title,
			creator=creator,
			description=description,
			subject=subject,
			transactionHash=transactionHash,
		)
		db.session.add(detail)
		db.session.commit()
		return redirect(url_for('asset.upload'))


	return render_template('web3/upload.html', creator=creator, address_NFT=address_NFT, NFT_abi=NFT_abi_json)


@mod.route('/asset_list', methods=['GET', 'POST'])
def asset_list():
	asset_detail = []
	asset_detail_list = []
	my_address = session['currentAccount']
	asset_list = db.session.query(Asset_nft) \
		.join(Asset_detail, Asset_nft.transactionHash == Asset_detail.transactionHash) \
		.add_columns(Asset_nft.NftId, Asset_detail.title, Asset_detail.subject, Asset_nft.operator, Asset_nft.transactionHash, Asset_nft.img) \
		.filter(Asset_nft.operator.like(my_address)) \
		.all()
	for asset in asset_list:
		# print(f'{asset}')
		asset_detail.append(asset.NftId)
		asset_detail.append(asset.title)
		asset_detail.append(asset.subject)
		asset_detail.append(asset.operator)
		asset_detail.append(asset.transactionHash)
		asset_detail.append(asset.img)
		asset_detail_list.append(asset_detail)
		asset_detail=[]

	# print(f'{asset_detail_list}')


	return render_template('web3/asset_list.html', asset_detail_list=asset_detail_list, asset_count=len(asset_detail_list))


@mod.route('/search', methods=['GET', 'POST'])
def search():  # 加入搜尋條件的商品列表
	asset_detail_list = search_core()
	return render_template('web3/asset_list.html', asset_detail_list=asset_detail_list, asset_count=len(asset_detail_list))


@mod.route('/asset_view/<transactionHash>', methods=['GET', 'POST'])
def asset_view(transactionHash):
	target = Asset_detail.query.filter_by(transactionHash=transactionHash) \
		.join(Asset_nft, Asset_detail.transactionHash == Asset_nft.transactionHash) \
		.add_columns(Asset_detail.title, Asset_detail.creator, Asset_detail.description, Asset_detail.subject, Asset_detail.transactionHash, Asset_nft.img)\
		.first()
	# print(f'{target}')
	img = target.img

	if request.method == 'POST':
		# 更新omekas和資料庫 metadata
		# 取得網頁中填入資料
		title = request.form.get('title')
		creator = request.form.get('creator')
		description = request.form.get('description')
		subject = request.form.get('subject')

		# omeka資料更新
		# omekas API
		omeka_auth = OmekaAPIClient(
			api_url='http://localhost:81/api',
			key_identity='C1qUawykxTyB61j1rf0DPwJw68z0RgZo',
			key_credential='SZtaDwSzUR357zI5z0qKW9S5cU9dSw96'
		)
		# 取得omeka目標資料
		data = omeka_auth.filter_items_by_property(
			filter_property='dcterms:source',
			filter_value=transactionHash,  # 目標sonrce欄位hash值
			filter_type='eq',
			page=1)
		item = data['results'][0]
		# 更新欄位內容
		new_item = deepcopy(item)
		new_item['dcterms:title'][0]['@value'] = title
		new_item['dcterms:creator'][0]['@value'] = creator
		new_item['dcterms:description'][0]['@value'] = description
		new_item['dcterms:subject'][0]['@value'] = subject
		# 上傳更新到omeka
		updated_item = omeka_auth.update_resource(new_item, resource_type='items')
		assert item['o:id'] == updated_item['o:id']
		print(f'Omeka Finish Update')

		# 資料庫更新
		update_target = Asset_detail.query.filter_by(transactionHash=transactionHash).first()

		update_target.title = title
		update_target.creator = creator
		update_target.description = description
		update_target.subject = subject
		db.session.commit()
		print(f'DB Finish Update')

		return render_template('web3/asset_view.html', target=target, img=img)

	return render_template('web3/asset_view.html', target=target, img=img)


@mod.route('/launch/<token_id>/<asset_title>', methods=['GET', 'POST'])
def launch(token_id, asset_title):

	return render_template('web3/launch.html', asset_title=asset_title, token_id=token_id, address_ART=address_ART, ART_abi=ART_abi_json)


def get_launch_detail_list():
	my_address = session['currentAccount']
	# 讀取合約中所有Launch事件
	to_block = chain.eth.blockNumber
	launch_detail_list = []
	event_filter = contract_ART.events['Launch'].createFilter(fromBlock=0, toBlock=to_block)
	for event in event_filter.get_all_entries():
		# 針對每個Launch事件檢查其launch_detail的status
		launch_detail = contract_ART.functions.launchDetail(event['args']['launchId']).call()
		if event['args']['operator'] == my_address and launch_detail[4]:
			# 若為真就加入list中
			launch_detail.append(event['args']['launchId'])
			launch_detail_list.append(launch_detail)
	print(f'{len(launch_detail_list)} Launch Detail {launch_detail_list}')
	return launch_detail_list


def sort(launch_detail_list):
	session['sort'] = request.form['sort']
	sort_key = ['title', 'days', 'price', 'hash', 'status', 'id', 'img']
	index = sort_key.index(request.form['sort'])
	launch_detail_list = sorted(launch_detail_list, key=lambda x: x[index])
	return launch_detail_list



@mod.route('/launched_assets', methods=['GET', 'POST'])
def launched_assets(): #商品下架
	launch_detail_list = get_launch_detail_list()

	print(f'Launch Detail {launch_detail_list}')
	asset_list = db.session.query(Asset_nft) \
		.join(Asset_detail, Asset_nft.transactionHash == Asset_detail.transactionHash) \
		.join(Launch_to_nft, Asset_nft.NftId == Launch_to_nft.tokenId) \
		.add_columns(Asset_nft.NftId, Asset_detail.title, Asset_detail.subject, Asset_detail.transactionHash, Asset_nft.img) \
		.all()
	print(f'asset_list - {asset_list}')

	if request.method == 'POST' and request.form['s_key'] and request.form['s_value']:
		session['s_key'] = request.form['s_key']
		session['s_value'] = request.form['s_value']
		if session['s_value'] == '':
			redirect(url_for('asset.launched_assets'))
		search_target = getattr(Asset_detail, session['s_key'])
		query = db.session.query(Asset_nft) \
			.join(Asset_detail, Asset_nft.transactionHash == Asset_detail.transactionHash) \
			.join(Launch_to_nft, Asset_nft.NftId == Launch_to_nft.tokenId) \
			.add_columns(Asset_nft.NftId, Asset_detail.title, Asset_detail.subject, Asset_detail.transactionHash, Asset_nft.img) \
			.filter(search_target.like('%' + session['s_value'] + '%'))
		asset_list = query.all()
		asset_list = [sublist[1:] for sublist in asset_list]
		launch_detail_list = [item for item in launch_detail_list if item[0] in [b[0] for b in asset_list]]
		asset_dict = {}
		for asset in asset_list:
			asset_dict[asset[0]] = asset[1], asset[3], asset[4]
		# print(asset_dict)
		# 遍歷每個 list，進行替換
		for launch_detail in launch_detail_list:
			value = asset_dict[launch_detail[0]]
			launch_detail.append(value[2])
			launch_detail[0] = value[0]
			# print(f'{launch_detail}')

		# print(f'{launch_detail_list}')
		# session['s_value'] = ''
		# if request.form['sort']:
		# 	launch_detail_list = sort(launch_detail_list)

		return render_template('web3/launched_assets.html', launch_detail_list=launch_detail_list, address_ART=address_ART, ART_abi=ART_abi_json)

	asset_list = [sublist[1:] for sublist in asset_list]
	for asset in asset_list:
		list(asset)
		# print(f'asset - {asset}')
	asset_dict = {}
	for asset in asset_list:
		asset_dict[asset[0]] = asset[1], asset[3], asset[4]
	# print(f'asset_dict - {asset_dict}')
	# 遍歷每個 list，進行替換
	for launch_detail in launch_detail_list:
		value = asset_dict[launch_detail[0]]
		launch_detail.append(value[2])
		launch_detail[0] = value[0]
		# print(f'{launch_detail}')
	# print(launch_detail_list)


	return render_template('web3/launched_assets.html', launch_detail_list=launch_detail_list, address_ART=address_ART, ART_abi=ART_abi_json)