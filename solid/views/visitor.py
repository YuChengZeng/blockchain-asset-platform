# -*- coding: utf-8 -*-
from copy import deepcopy
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
from solid.models.set_room import Set_room
from solid.models.room_list import Room_list
from solid.models.ticket import Ticket
from solid.models.pi_user import Pi_user
from solid.models.launch_to_nft import Launch_to_nft
import json
from web3 import Web3
from web3.auto import w3
from web3.middleware import geth_poa_middleware
from web3.exceptions import TransactionNotFound
from werkzeug.utils import secure_filename
from omeka_s_tools.api import OmekaAPIClient


mod = Blueprint('visitor', __name__)
CORS(mod)

@mod.route('/room_list', methods=['GET', 'POST'])
def room_list():
	# 已設定票價展間列表
	room_list = db.session.query(Room_list) \
		.join(Set_room, Set_room.room_id == Room_list.room_id) \
		.with_entities(Room_list, Set_room.room_id) \
		.add_columns(Room_list.title, Room_list.coverUrl, Room_list.signboardUrl, Room_list.introduction, Set_room.price) \
		.filter(Set_room.price != 0) \
		.all()
	# print(room_list)

	return render_template('web3/room_list.html', rooms=room_list, address_TT=address_TT, TT_abi=TT_abi_json, address_CT=address_CT, CT_abi=CT_abi_json)


@mod.route('/my_room', methods=['GET', 'POST'])
def my_room():
	# 已設定票價展間列表
	currentAccount = session['currentAccount']
	room_list = db.session.query(Set_room) \
		.filter(Set_room.address.like(currentAccount)) \
		.join(Room_list, Set_room.room_id == Room_list.room_id) \
		.with_entities(Room_list, Set_room.room_id) \
		.add_columns(Room_list.title, Room_list.coverUrl, Room_list.signboardUrl, Room_list.introduction, Set_room.price) \
		.filter(Set_room.price != 0) \
		.all()

	# print(room_list)

	return render_template('web3/my_room.html', rooms=room_list, address_TT=address_TT, TT_abi=TT_abi_json, address_CT=address_CT, CT_abi=CT_abi_json)


@mod.route('/for_class', methods=['GET', 'POST'])
def for_class():
	if request.method == 'POST':
		account = request.form['account']
		target_user = db.session.query(Pi_user) \
			.filter(Pi_user.email.like(account)) \
			.first()
		if target_user is not None:
			currentAccount = target_user.address

			room_list = db.session.query(Set_room) \
				.filter(Set_room.address.like(currentAccount)) \
				.join(Room_list, Set_room.room_id == Room_list.room_id) \
				.with_entities(Room_list, Set_room.room_id) \
				.add_columns(Room_list.title, Room_list.coverUrl, Room_list.signboardUrl, Room_list.introduction,
							 Set_room.price) \
				.filter(Set_room.price != 0) \
				.all()

			# print(room_list)

			return render_template('web3/for_class.html', rooms=room_list, address_TT=address_TT, TT_abi=TT_abi_json,
							   address_CT=address_CT, CT_abi=CT_abi_json)
	return render_template('web3/for_class.html', address_TT=address_TT, TT_abi=TT_abi_json,
						   address_CT=address_CT, CT_abi=CT_abi_json)


@mod.route('/check_ticket/<room_id>', methods=['GET', 'POST'])
def check_ticket(room_id):
	# 驗票
	my_address = session['currentAccount']
	has_ticket = db.session.query(Ticket).filter(
		Ticket.room_id == room_id,
		Ticket.address == my_address,
	).first()
	if has_ticket is None:
		return '0'
	else:
		return '1'