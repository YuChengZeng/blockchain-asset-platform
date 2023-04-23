# -*- coding: utf-8 -*-
from datetime import datetime
import os
from eth_account.messages import encode_defunct
from flask import Blueprint, render_template, jsonify, redirect, url_for, request, g, session, flash, Flask, make_response
from flask_cors import cross_origin
from flask_cors import CORS
from collections import Counter
import time
from re import escape
from sqlalchemy.exc import SQLAlchemyError
from solid.extension import db
from solid.views.misc import items_pagebar, last_page
from solid.views.config import *  # if for PyCharm execution, use script.config
# from solid.views.filter import *
from solid.models.interact import Interact
from solid.models.token import Token
from solid.models.asset_detail import Asset_detail
from solid.models.asset_nft import Asset_nft
from solid.models.launch_to_nft import Launch_to_nft
from solid.models.application_list import Application_list
from solid.models.ticket import Ticket
from solid.models.room_list import Room_list
from solid.models.set_room import Set_room

import json
from web3 import Web3
from web3.auto import w3
from web3.middleware import geth_poa_middleware
from web3.exceptions import TransactionNotFound
from solid.models.user import User
from werkzeug.utils import secure_filename
from omeka_s_tools.api import OmekaAPIClient

mod = Blueprint('web3', __name__)
CORS(mod)


@mod.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
	my_address = session['currentAccount']
	my_balance = contract_CT.functions.balanceOf(my_address).call()
	revenue_ART = contract_ART.functions.revenue(my_address).call()
	revenue_TT = contract_TT.functions.revenue(my_address).call()

	# 租用商品花費
	query_application = db.session.query(Application_list) \
		.filter(Application_list.operator.like(my_address)) \
		.join(Launch_to_nft, Launch_to_nft.launch_id == Application_list.launchId) \
		.join(Asset_nft, Asset_nft.NftId == Launch_to_nft.tokenId) \
		.join(Asset_detail, Asset_detail.transactionHash == Asset_nft.transactionHash) \
		.add_columns(Launch_to_nft.tokenId, Asset_detail.title, Asset_detail.creator,
					 Asset_detail.description, Asset_detail.subject, Asset_detail.transactionHash, Application_list.price) \
		.all()

	# print(f'query_application{query_application}')
	expense_application = 0
	for item in query_application:
		expense_application += item.price
	print(f'expense_application{expense_application}')

	# 購買門票花費
	query_ticket = db.session.query(Ticket) \
		.filter(Ticket.address.like(my_address)) \
		.join(Room_list, Room_list.room_id == Ticket.room_id) \
		.add_columns(Ticket.room_id, Room_list.title, Ticket.price) \
		.all()
	# print(f'query_ticket{query_ticket}')
	expense_ticket = 0
	for item in query_ticket:
		expense_ticket += item.price
	print(f'expense_ticket{expense_ticket}')

	# 商品收入
	query_commodities = db.session.query(Application_list) \
		.join(Launch_to_nft, Launch_to_nft.launch_id == Application_list.launchId) \
		.join(Asset_nft, Asset_nft.NftId == Launch_to_nft.tokenId) \
		.join(Asset_detail, Asset_detail.transactionHash == Asset_nft.transactionHash) \
		.filter(Launch_to_nft.operator.like(my_address)) \
		.add_columns(Asset_detail.title, Asset_detail.creator, Asset_detail.description, Asset_detail.subject, Application_list.price) \
		.all()
	# print(f'query_commodities{query_commodities}')

	revenue_commodities = 0
	for item in query_commodities:
		revenue_commodities += item.price
	print(f'revenue_commodities{revenue_commodities}')

	# 門票收入
	query_ticket_revenue = db.session.query(Ticket) \
		.join(Set_room, Set_room.room_id == Ticket.room_id) \
		.join(Room_list, Room_list.room_id == Ticket.room_id) \
		.filter(Set_room.address.like(my_address)) \
		.add_columns(Room_list.room_id, Room_list.title, Ticket.price) \
		.all()
	revenue_ticket = 0
	for item in query_ticket_revenue:
		revenue_ticket += item.price
	print(f'revenue_ticket{revenue_ticket}')




	# 展間互動收入
	query_interact_revenue = db.session.query(Interact) \
		.filter(Interact.address.like(my_address))
	revenue_interact = len(query_interact_revenue.all())*100
	print(revenue_interact)

	revenue_RWD = len(query_interact_revenue.filter(Interact.status.like('1')).all())*100
	print(revenue_RWD)
	if request.method == 'POST':
		interact_status = db.session.query(Interact) \
			.filter(Interact.address.like(my_address)) \
			.filter(Interact.status.like('1')) \
			.all()
		for interact in interact_status:
			interact.status = 0
			db.session.commit()

	return render_template('web3/withdraw.html', my_balance=my_balance,
						   expense_application=expense_application, expense_ticket=expense_ticket,
						   revenue_commodities=revenue_commodities, revenue_ticket=revenue_ticket, revenue_interact=revenue_interact,
						   address_ART=address_ART, ART_abi=ART_abi_json, address_TT=address_TT, TT_abi=TT_abi_json, address_CT=address_CT, CT_abi=CT_abi_json,
						   revenue_ART=revenue_ART, revenue_TT=revenue_TT, revenue_RWD=revenue_RWD)


@mod.route('/instruction', methods=['GET', 'POST'])
def instruction():
	return render_template('web3/instruction.html', address_CT=address_CT, CT_abi=CT_abi_json, address_ART=address_ART, address_TT=address_TT)


@mod.route('/commodities_rank', methods=['GET', 'POST'])
def commodities_rank():
	query = db.session.query(Application_list) \
		.join(Launch_to_nft, Launch_to_nft.launch_id == Application_list.launchId) \
		.join(Asset_nft, Asset_nft.NftId == Launch_to_nft.tokenId) \
		.join(Asset_detail, Asset_detail.transactionHash == Asset_nft.transactionHash) \
		.add_columns(Launch_to_nft.tokenId, Asset_detail.title, Asset_detail.creator, Asset_detail.description, Asset_detail.subject, Asset_detail.transactionHash)
	application_list = query.all()
	application_list = [sublist[1:] for sublist in application_list]
	application_list = Counter(application_list)
	# print(application_list)
	commodities_rank = []
	for key, value in application_list.items():
		commodities_rank.append([key[0], key[1], key[2], key[3], key[4], key[5], value])

	# print(commodities_rank)
	return render_template('web3/commodities_rank.html', commodities_rank=commodities_rank)


@mod.route('/room_rank', methods=['GET', 'POST'])
def room_rank():
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
	return render_template('web3/room_rank.html', ticket_rank=ticket_rank)


@mod.route('/add_to_collect', methods=['POST'])
def add_to_collect():
	item_type = request.form['collect_type']
	item_id = request.form['collect_Id']
	item = [[item_type, item_id]]
	if item[0] not in session['cart']:
		session['cart'] = session['cart'] + item # 將商品加入 cart List
	print(session['cart'])
	return '', 204


@mod.route('/collection', methods=['GET', 'POST'])
def collection():
	if request.method == 'POST':
		session['cart'] = []
	collection_list = session['cart']
	commodities = []
	rooms = []
	for type in collection_list:
		if type[0] == 'c':
			commodities.append(type)
		else:
			rooms.append(type)

	asset_list = []
	for item in commodities:
		# print(item)
		query = db.session.query(Asset_nft) \
			.filter(Asset_nft.NftId == item[1]) \
			.join(Asset_detail, Asset_nft.transactionHash == Asset_detail.transactionHash) \
			.add_columns(Asset_nft.NftId, Asset_detail.title, Asset_detail.subject, Asset_detail.transactionHash, Asset_nft.img) \
			.all()
		for asset in query:
			asset_list.append(asset)

	room_list = []
	for item in rooms:
		# print(item)
		query = db.session.query(Room_list) \
			.filter(Room_list.room_id == item[1]) \
			.join(Set_room, Set_room.room_id == Room_list.room_id) \
			.add_columns(Room_list.title, Room_list.coverUrl, Room_list.signboardUrl, Room_list.introduction, Set_room.price, Room_list.room_id) \
			.all()
		for room in query:
			room_list.append(room)
	print(asset_list)
	print(room_list)

	return render_template('web3/collection.html', asset_list=asset_list, room_list=room_list)

