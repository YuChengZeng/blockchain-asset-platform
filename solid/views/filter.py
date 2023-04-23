# -*- coding: utf-8 -*-
from datetime import datetime
import os
from eth_account.messages import encode_defunct
from flask import Blueprint, render_template, jsonify, redirect, url_for, request, g, session, flash, Flask
from flask_cors import cross_origin
from flask_cors import CORS
import time
from re import escape
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql.elements import and_

from solid.extension import db
from solid.views.misc import items_pagebar, last_page
from solid.models.token import Token
from solid.models.asset_detail import Asset_detail
from solid.models.asset_nft import Asset_nft
from solid.models.launch_to_nft import Launch_to_nft
from solid.models.pi_user import Pi_user
from solid.models.set_room import Set_room
from solid.models.ticket import Ticket
from solid.models.interact import Interact
import json
from solid.views.config import *  # if for PyCharm execution, use script.config
from web3 import Web3
from web3.auto import w3
from web3.middleware import geth_poa_middleware
from web3.exceptions import TransactionNotFound
from solid.models.user import User
from werkzeug.utils import secure_filename
import requests
from omeka_s_tools.api import OmekaAPIClient

mod = Blueprint('filter', __name__)
CORS(mod)


@mod.route('/source', methods=['GET', 'POST'])
@mod.route('/source/<transactionHash>', methods=['GET', 'POST'])
def source(transactionHash):
	omeka_auth = OmekaAPIClient(
		api_url='http://localhost:81/api',
		key_identity='fumP6KLVevGGOBYVy4c7C7kcLLr25eXa',
		key_credential='rrE5dnK4M52IOhL4sXo2GgjdipmGtw8Q'
	)

	item = omeka_auth.filter_items_by_property(
		filter_property='dcterms:source',
		filter_value=transactionHash,  # 目標sonrce欄位hash值
		filter_type='eq',
		page=1)
	url = item['results'][0]["thumbnail_display_urls"]["square"]
	relative_url = url.replace("http://localhost:81/api", "https://blockchain-omekas.dlll.nccu.edu.tw")

	# return redirect(relative_url)
	return relative_url


@mod.route('/licence_check/<_id>', methods=['GET', 'POST'])
def licence_check(_id):
	# 給使用者_id
	# 回傳使用者的授權和期限內憑證的到期日
	target_user = Pi_user.query.filter_by(_id=_id).first()
	address = target_user.address
	chain = Web3(Web3.HTTPProvider(RPC_URI))  # set web3 target
	to_block = chain.eth.blockNumber
	# load contract
	with open('/root/output/' + 'AssetRental' + '.abi', 'r') as f:
		abi_json = f.readline()
	abi = json.loads(abi_json)
	target_contract = chain.eth.contract(address=address_ART, abi=abi)

	license_list = []
	# fetch Application event
	event_filter = target_contract.events['Application'].createFilter(fromBlock=0, toBlock=to_block)
	for event in event_filter.get_all_entries():
		# 過濾錢包擁有者的event
		if event['args']['operator'] == address:
			license_list.append(event['args']['licenseId'])
	# 地址擁有的全部憑證
	print(f'Users all license {license_list}')
	license_detail_list = []
	for license in license_list:
		# 檢查每個憑證的有效日期
		license_detail = target_contract.functions.licenseDetail(license).call()
		print(f'License EXP {license_detail[1]} Now {time.time()}')
		if license_detail[1] >= time.time():
			struct_time = time.localtime(license_detail[1])
			exp_date = time.strftime("%Y/%m/%d %H:%M:%S", struct_time)
			license_detail[1] = exp_date
			# 如果在期限內則加入列表準備回傳
			license_detail_list.append(license_detail)
	print(f'License Detail List {license_detail_list}')

	licence_list = []
	for license_detail in license_detail_list:
		licence_dict = {'license_id': license_detail[0], 'exp_date': license_detail[1]}
		licence_list.append(licence_dict)

	licence_json = json.dumps(licence_list)

	return licence_json


@mod.route('/api_interactExisting', methods=['POST'])
def api_interactExisting():
	result = request.get_json(force=True)
	# 檢查是否已存在資料庫
	target_user = Pi_user.query.filter_by(_id=result['uid']).first()
	address = target_user.address
	existing_data = db.session.query(Interact).filter(
		and_(Interact.address == address, Interact.room_id == result['roomId'], Interact.target == result['target'])
	).first()
	if existing_data:
		print('1')
		return '1'
	else:
		print('0')
		return '0'


@mod.route('/api_exhInteract', methods=['GET', 'POST'])
def api_exhInteract():
	result = request.get_json(force=True)
	# 互動結果記錄到資料庫
	target_user = Pi_user.query.filter_by(_id=result['uid']).first()
	address = target_user.address
	existing_data = db.session.query(Interact).filter(
		and_(Interact.address == address, Interact.room_id == result['roomId'], Interact.target == result['target'])
	).first()
	if existing_data:
		print(f'Already')
	else:
		# 新增資料
		data = Interact(
			address=address,
			room_id=result['roomId'],
			target=result['target'],
			interact=result['interact'],
			status='1'
		)
		db.session.add(data)
		db.session.commit()
		print(f'Interaction Detected')

	return jsonify(result)


@mod.route('/api_licence_list/<_id>', methods=['GET', 'POST'])
def api_licence_list(_id):
	to_block = chain.eth.blockNumber
	target_user = Pi_user.query.filter_by(_id=_id).first()
	address = target_user.address

	license_list = []
	# fetch Application event
	event_filter = contract_ART.events['Application'].createFilter(fromBlock=0, toBlock=to_block)
	for event in event_filter.get_all_entries():
		# 過濾錢包擁有者的event
		if event['args']['operator'] == address:
			license_list.append(event['args']['licenseId'])
	print(f'Users all license {license_list}')
	license_detail_list = []
	for license in license_list:
		license_detail = contract_ART.functions.licenseDetail(license).call()
		print(f'License EXP {license_detail[1]} Now {time.time()}')
		if license_detail[1] >= time.time():
			struct_time = time.localtime(license_detail[1])
			exp_date = time.strftime("%Y/%m/%d %H:%M:%S", struct_time)
			license_detail[1] = exp_date
			license_detail_list.append(license_detail)
	print(f'License Detail List {license_detail_list}')

	asset_list = db.session.query(Asset_nft) \
		.join(Asset_detail, Asset_nft.transactionHash == Asset_detail.transactionHash) \
		.join(Launch_to_nft, Asset_nft.NftId == Launch_to_nft.tokenId) \
		.add_columns(Asset_nft.NftId, Asset_detail.title, Asset_detail.subject, Asset_detail.transactionHash,
					 Asset_nft.img) \
		.all()
	print(asset_list)
	asset_list = [sublist[1:] for sublist in asset_list]

	for asset in asset_list:
		list(asset)
		print(f'{asset}')
	asset_dict = {}
	for asset in asset_list:
		asset_dict[asset[0]] = asset[1], asset[3], asset[4]
	print(f'Asset Dict{asset_dict}')
	# 遍歷每個 list，進行替換
	for license_detail in license_detail_list:
		title = asset_dict[license_detail[0]][0]
		license_detail.append(asset_dict[license_detail[0]][2])
		license_detail[0] = title
		print(f'{license_detail}')

	license_detail_list = [{'title': i[0], 'exp_date': i[1], 'img_url': i[2]} for i in license_detail_list]

	# for license_detail in license_detail_list:
	# 	licence_dict = {'NFT_id': license_detail[0], 'exp_date': license_detail[1], 'title': license_detail[2],
	# 					'subject': license_detail[3], 'transactionHash': license_detail[4], 'img_url': license_detail[5]}
	# 	licence_list.append(licence_dict)
	licence_list_json = json.dumps(license_detail_list)

	return licence_list_json


@mod.route('/api_inEXP/<_id>', methods=['GET', 'POST'])
def api_inEXP(_id):
	# 檢查使用者ID回傳租期內的檔案連結
	target_user = Pi_user.query.filter_by(_id=_id).first()
	address = target_user.address

	chain = Web3(Web3.HTTPProvider(RPC_URI))  # set web3 target
	to_block = chain.eth.blockNumber
	# load contract
	with open('/root/output/' + 'AssetRental' + '.abi', 'r') as f:
		abi_json = f.readline()
	abi = json.loads(abi_json)
	target_contract = chain.eth.contract(address=address_ART, abi=abi)
	license_list = []
	# fetch Application event
	event_filter = target_contract.events['Application'].createFilter(fromBlock=0, toBlock=to_block)
	for event in event_filter.get_all_entries():
		# 過濾錢包擁有者的event
		if event['args']['operator'] == address:
			license_list.append(event['args']['licenseId'])
	# 地址擁有的全部憑證
	print(f'Users all license {license_list}')

	inEXP_list = []
	inEXP_url_dict = {}
	for license in license_list:
		license_detail = target_contract.functions.licenseDetail(license).call()
		print(f'License EXP {license_detail[1]} Now {time.time()}')
		if license_detail[1] >= time.time():
			inEXP_list.append(license_detail[0])
	print(f'Assets inEXP {inEXP_list}')
	for i in inEXP_list:
		urls = Asset_nft.query.filter_by(NftId=i).first()
		key = i
		value = urls.img
		inEXP_url_dict[key] = value
	print(f'{inEXP_url_dict}')

	return inEXP_url_dict


@mod.route('/api_exhEXP/<room_id>', methods=['GET', 'POST'])
def api_exhEXP(room_id):
	# 檢查room_id回傳租期內的檔案連結
	target_user = Set_room.query.filter_by(room_id=room_id).first()
	address = target_user.address

	chain = Web3(Web3.HTTPProvider(RPC_URI))  # set web3 target
	to_block = chain.eth.blockNumber
	# load contract
	with open('/root/output/' + 'AssetRental' + '.abi', 'r') as f:
		abi_json = f.readline()
	abi = json.loads(abi_json)
	target_contract = chain.eth.contract(address=address_ART, abi=abi)
	license_list = []
	# fetch Application event
	event_filter = target_contract.events['Application'].createFilter(fromBlock=0, toBlock=to_block)
	for event in event_filter.get_all_entries():
		# 過濾錢包擁有者的event
		if event['args']['operator'] == address:
			license_list.append(event['args']['licenseId'])
	# 地址擁有的全部憑證
	print(f'Users all license {license_list}')

	inEXP_list = []
	inEXP_url_dict = {}
	for license in license_list:
		license_detail = target_contract.functions.licenseDetail(license).call()
		print(f'License EXP {license_detail[1]} Now {time.time()}')
		if license_detail[1] >= time.time():
			inEXP_list.append(license_detail[0])
	print(f'Assets inEXP {inEXP_list}')
	for i in inEXP_list:
		urls = Asset_nft.query.filter_by(NftId=i).first()
		key = i
		value = urls.img
		inEXP_url_dict[key] = value
	print(f'{inEXP_url_dict}')

	return inEXP_url_dict


@mod.route('/api_ticket/<_id>/<room_id>', methods=['GET', 'POST'])
def api_ticket(_id, room_id):
	# 檢查使用者ID是否有展間門票
	target_user = Pi_user.query.filter_by(_id=_id).first()
	address = target_user.address
	print('---------------------------------------')
	print(_id)
	print(room_id)
	print('---------------------------------------')
	verified_room = []
	tickets = Ticket.query.filter_by(address=address).all()
	for ticket in tickets:
		verified_room.append(ticket.room_id)
	if room_id in verified_room:
		return '1'
	else:
		return '0'
