# -*- coding: utf-8 -*-
import json
from datetime import datetime
import time
import requests
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from web3 import Web3
from web3.middleware import geth_poa_middleware
from web3.exceptions import TransactionNotFound
from model import *  # if for PyCharm execution, use script.model
from config import *  # if for PyCharm execution, use script.config
from omeka_s_tools.api import OmekaAPIClient
import binascii
import asyncio



def test(chain, session):  # fetch SetRoom event to DB
	my_address = '0xF96f60CA84A07094c9fC5b3eBb63A19090D5EEd8'
	my_balance = contract_CT.functions.balanceOf(my_address).call()
	revenue_ART = contract_ART.functions.revenue(my_address).call()
	revenue_TT = contract_TT.functions.revenue(my_address).call()

	# 租用商品花費
	query_application = session.query(Application_list) \
		.filter(Application_list.operator.like(my_address)) \
		.join(Launch_to_nft, Launch_to_nft.launch_id == Application_list.launchId) \
		.join(Asset_nft, Asset_nft.NftId == Launch_to_nft.tokenId) \
		.join(Asset_detail, Asset_detail.transactionHash == Asset_nft.transactionHash) \
		.add_columns(Launch_to_nft.tokenId, Asset_detail.title, Asset_detail.creator,
					 Asset_detail.description, Asset_detail.subject, Asset_detail.transactionHash,
					 Application_list.price) \
		.all()

	# print(f'query_application{query_application}')
	expense_application = 0
	for item in query_application:
		expense_application += item.price
	print(f'expense_application {expense_application}')

	# 購買門票花費
	query_ticket = session.query(Ticket) \
		.filter(Ticket.address.like(my_address)) \
		.join(Room_list, Room_list.room_id == Ticket.room_id) \
		.add_columns(Ticket.room_id, Room_list.title, Ticket.price) \
		.all()
	# print(f'query_ticket{query_ticket}')
	expense_ticket = 0
	for item in query_ticket:
		expense_ticket += item.price
	print(f'expense_ticket {expense_ticket}')

	# 商品收入
	query_commodities = session.query(Application_list) \
		.join(Launch_to_nft, Launch_to_nft.launch_id == Application_list.launchId) \
		.join(Asset_nft, Asset_nft.NftId == Launch_to_nft.tokenId) \
		.join(Asset_detail, Asset_detail.transactionHash == Asset_nft.transactionHash) \
		.filter(Launch_to_nft.operator.like(my_address)) \
		.add_columns(Asset_detail.title, Asset_detail.creator, Asset_detail.description, Asset_detail.subject,
					 Application_list.price) \
		.all()
	# print(f'query_commodities{query_commodities}')

	revenue_commodities = 0
	for item in query_commodities:
		revenue_commodities += item.price
	print(f'revenue_commodities {revenue_commodities}')

	# 門票收入
	query_ticket_revenue = session.query(Ticket) \
		.join(Set_room, Set_room.room_id == Ticket.room_id) \
		.join(Room_list, Room_list.room_id == Ticket.room_id) \
		.filter(Set_room.address.like(my_address)) \
		.add_columns(Room_list.room_id, Room_list.title, Ticket.price) \
		.all()
	revenue_ticket = 0
	for item in query_ticket_revenue:
		revenue_ticket += item.price
	print(f'revenue_ticket {revenue_ticket}')

	# 展間互動收入
	query_interact_revenue = session.query(Interact) \
		.filter(Interact.address.like(my_address))
	revenue_interact = len(query_interact_revenue.all()) * 100
	print(f'revenue_interact {revenue_interact}')

def main():
	# sqlalchemy init
	engine = create_engine(SQLALCHEMY_HOST_URI)
	Session = sessionmaker(bind=engine)
	session = Session()

	skychain = Web3(Web3.HTTPProvider('https://rpc.skychainnet.com'))  # set web3 target
	skychain.middleware_onion.inject(geth_poa_middleware, layer=0)


	test(skychain, session)


if __name__ == "__main__":
	main()