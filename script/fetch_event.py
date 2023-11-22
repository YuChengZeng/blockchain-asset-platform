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


async def source(transactionHash):
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
	if not item['results']:
		print('Can,t find resource in Omeka')
		relative_url = ''
	else:
		format = item['results'][0]["dcterms:format"][0]["@value"]
		if format == "video":
			item_url = item['results'][0]["o:media"][0]["@id"]
			print(item_url)
			result = requests.get(item_url)
			url = result.json()['o:original_url']
			relative_url = url.replace("http://localhost:81/", "https://blockchain-omekas.dlll.nccu.edu.tw/")
			print(relative_url)
		elif format == "image":
			url = item['results'][0]["thumbnail_display_urls"]["square"]
			relative_url = url.replace("http://localhost:81/", "https://blockchain-omekas.dlll.nccu.edu.tw/")
	return relative_url


async def fetch_Nft_mint(chain, session):
	row = session.query(Asset_nft).order_by(Asset_nft.blockNumber.desc()).first()
	if not row:
		from_block = 0
	else:
		from_block = row.blockNumber + 1
	to_block = chain.eth.blockNumber
	# load contract
	with open('/root/output/' + 'Nft' + '.abi', 'r') as f:
		abi_json = f.readline()
	abi = json.loads(abi_json)
	target_contract = chain.eth.contract(address=address_NFT, abi=abi)
	# 讀取合約中所有Nft_mint事件
	event_filter = target_contract.events['Nft_mint'].createFilter(fromBlock=from_block, toBlock=to_block)
	i = 0
	for entry in event_filter.get_all_entries():
		print(entry)
		print(entry['args']['NftId'], entry['args']['sha'], entry['args']['time'], entry['args']['operator'],
			  entry['transactionHash'].hex(), entry['blockNumber'])
		transactionHash = str(entry['transactionHash'].hex())
		print(transactionHash)
		img = await source(transactionHash)
		# print(img)
		if not img:
			new_event = Asset_nft(
				NftId=entry['args']['NftId'],
				sha=entry['args']['sha'],
				time=entry['args']['time'],
				operator=entry['args']['operator'],
				transactionHash=transactionHash,
				blockNumber=entry['blockNumber'],
				source=''
			)
			session.add(new_event)
			session.commit()
			i += 1
		else:
			new_event = Asset_nft(
				NftId=entry['args']['NftId'],
				sha=entry['args']['sha'],
				time=entry['args']['time'],
				operator=entry['args']['operator'],
				transactionHash=transactionHash,
				blockNumber=entry['blockNumber'],
				source=img
			)
			session.add(new_event)
			session.commit()
			i += 1
	print('%d new Nft_mint events' % i)


def launch2nft(chain, session):  # 透過fetch Launch event 結合tokenId和launchId
	row = session.query(Launch_to_nft).order_by(Launch_to_nft.blockNumber.desc()).first()
	if not row:
		from_block = 0
	else:
		from_block = row.blockNumber + 1
	to_block = chain.eth.blockNumber
	# load contract
	with open('/root/output/' + 'AssetRental' + '.abi', 'r') as f:
		abi_json = f.readline()
	abi = json.loads(abi_json)
	target_contract = chain.eth.contract(address=address_ART, abi=abi)
	event_filter = target_contract.events['Launch'].createFilter(fromBlock=from_block, toBlock=to_block)
	# print(event_filter.get_all_entries())
	i = 0
	for entry in event_filter.get_all_entries():
		print(entry['args']['launchId'], entry['args']['cnftId'], entry['args']['operator'], entry['args']['price'], entry['blockNumber'])
		new_event = Launch_to_nft(
			launch_id=entry['args']['launchId'],
			tokenId=entry['args']['cnftId'],
			operator=entry['args']['operator'],
			status=True,
			price=entry['args']['price'],
			blockNumber=entry['blockNumber']
		)
		session.add(new_event)
		session.commit()
		i += 1
	print(f'{i} new Launch events')


def status(chain, session):  # 資料庫更新下架紀錄
	row = session.query(Launch_to_nft).order_by(Launch_to_nft.blockNumber.desc()).first()
	if not row:
		from_block = 0
	else:
		from_block = row.blockNumber + 1
	to_block = chain.eth.blockNumber
	# load contract
	with open('/root/output/' + 'AssetRental' + '.abi', 'r') as f:
		abi_json = f.readline()
	abi = json.loads(abi_json)
	target_contract = chain.eth.contract(address=address_ART, abi=abi)

	launch_detail_list = []
	# 讀取合約中所有LaunchStatus事件
	i = 0
	event_filter = target_contract.events['LaunchStatus'].createFilter(fromBlock=from_block, toBlock=to_block)
	for event in event_filter.get_all_entries():
		# 針對每個LaunchStatus事件直接改資料庫內資料
		launch_detail = target_contract.functions.launchDetail(event['args']['launchId']).call()
		status = session.query(Launch_to_nft).filter_by(launch_id=launch_detail[0]).first()
		if status is not None:
			status.status = launch_detail[4]
			session.commit()
			i += 1
	print(f'{i} Launch Status Changed')


def set_room(chain, session):  # fetch SetRoom event to DB
	row = session.query(Set_room).order_by(Set_room.blockNumber.desc()).first()
	if not row:
		from_block = 0
	else:
		from_block = row.blockNumber + 1
	to_block = chain.eth.blockNumber
	# load contract
	with open('/root/output/' + 'Tickets' + '.abi', 'r') as f:
		abi_json = f.readline()
	abi = json.loads(abi_json)
	target_contract = chain.eth.contract(address=address_TT, abi=abi)

	# 讀取合約中所有SetPrice事件
	i = 0
	event_filter = target_contract.events['SetPrice'].createFilter(fromBlock=from_block, toBlock=to_block)
	for event in event_filter.get_all_entries():
		room_id = event['args']['roomId']
		# 資料庫更新
		update_target = session.query(Set_room).filter_by(room_id=room_id).first()
		if update_target is not None:
			update_target.address = event['args']['roomOwner']
			update_target.price = event['args']['price']
			update_target.blockNumber = event['blockNumber']
			session.commit()
			i += 1
	print(f'{i} new room Room/Price Set')


def buy_ticket(chain, session):  # fetch BuyTicket event to DB
	row = session.query(Ticket).order_by(Ticket.blockNumber.desc()).first()
	if not row:
		from_block = 0
	else:
		from_block = row.blockNumber + 1
	to_block = chain.eth.blockNumber
	# 讀取合約中所有BuyTicket事件
	i = 0
	event_filter = contract_TT.events['BuyTicket'].createFilter(fromBlock=from_block, toBlock=to_block)
	for event in event_filter.get_all_entries():
		# 針對每個BuyTicket事件直接改資料庫內資料
		new_ticket = Ticket(
			address=event['args']['buyer'],
			ticket_id=event['args']['ticketId'],
			room_id=event['args']['roomId'],
			price=event['args']['price'],
			blockNumber=event['blockNumber']
		)
		session.add(new_ticket)
		session.commit()
		i += 1
	print(f'{i} BuyTicket events')


def get_room_list(session):
	# 展間列表
	url = 'https://dev-partyisland.dlll.nccu.edu.tw/api/exhibitions'
	response = requests.get(url)
	data_dict = json.loads(response.text)

	# print(f'data_dict {data_dict}')
	i = 0
	rooms = data_dict['data']['list']
	for room in rooms:
		# print(room['_id'])
		room_data = session.query(Room_list).filter_by(room_id=room['_id']).first()
		if room_data is None:
			# 如果 room_data 為 None，表示資料庫中沒有該筆資料，進行新增操作
			new_room = Room_list(
				room_id=room['_id'],
				coverUrl=room['coverUrl'],
				signboardUrl=room['signboardUrl'],
				title=room['title'],
				introduction=room['introduction']
			)
			session.add(new_room)
			session.commit()
			i += 1
		else:
			# 如果 room_data 不為 None，表示該筆資料已存在，直接使用即可
			# 資料庫更新
			room_update = session.query(Room_list).filter_by(room_id=room['_id']).first()
			room_update.coverUrl = room['coverUrl']
			room_update.signboardUrl = room['signboardUrl']
			room_update.title = room['title']
			room_update.introduction = room['introduction']
			session.commit()
	print(f'{i} new room finish setting')


def fetch_application(chain, session):
	row = session.query(Application_list).order_by(Application_list.blockNumber.desc()).first()
	if not row:
		from_block = 0
	else:
		from_block = row.blockNumber + 1
	to_block = chain.eth.blockNumber
	# load contract
	i = 0
	# 讀取合約中所有SetRoom事件
	event_filter = contract_ART.events['Application'].createFilter(fromBlock=from_block, toBlock=to_block)
	for event in event_filter.get_all_entries():
		# print(event['args'], event['blockNumber'])
		new_application = Application_list(
			operator=event['args']['operator'],
			licenseId=event['args']['licenseId'],
			launchId=event['args']['launchId'],
			price=event['args']['price'],
			blockNumber=event['blockNumber']
		)
		session.add(new_application)
		session.commit()
		i += 1
	print(f'{i} new Application event')



def test(chain, session):
	to_block = chain.eth.blockNumber
	# load contract
	with open('/root/output/' + 'AssetRental' + '.abi', 'r') as f:
		abi_json = f.readline()
	abi = json.loads(abi_json)
	target_contract = chain.eth.contract(address=address_ART, abi=abi)
	event_filter = target_contract.events['Launch'].createFilter(fromBlock=0, toBlock=to_block)
	# print(event_filter.get_all_entries())
	i = 0
	for entry in event_filter.get_all_entries():
		print(entry['args']['launchId'], entry['args']['cnftId'], entry['args']['operator'], entry['blockNumber'])


# license_detail_list = []
# for license in license_list:
# 	license_detail = target_contract.functions.license_detail(license).call()
# 	print(license_detail[1], time.time())
# 	if license_detail[1] >= time.time():
# 		struct_time = time.localtime(license_detail[1])
# 		exp_date = time.strftime("%Y/%m/%d %H:%M:%S", struct_time)
# 		license_detail[1] = exp_date
# 		license_detail_list.append(license_detail)
# print(license_detail_list)

def main():
	# sqlalchemy init
	engine = create_engine(SQLALCHEMY_HOST_URI)
	Session = sessionmaker(bind=engine)
	session = Session()

	skychain = Web3(Web3.HTTPProvider(RPC_URI))  # set web3 target
	skychain.middleware_onion.inject(geth_poa_middleware, layer=0)

	asyncio.run(fetch_Nft_mint(skychain, session))
	launch2nft(skychain, session)
	status(skychain, session)
	set_room(skychain, session)
	buy_ticket(skychain, session)
	get_room_list(session)
	fetch_application(chain, session)


# test_license_detail_list(skychain)


if __name__ == "__main__":
	main()
