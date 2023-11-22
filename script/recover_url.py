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


async def source(transactionHash, NftId):
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
		print(f'Can,t find resource in Omeka... id: {NftId}')
		relative_url = ''
	else:
		format = item['results'][0]["dcterms:format"][0]["@value"]
		if format == "video":
			item_url = item['results'][0]["o:media"][0]["@id"]
			# print(item_url)
			result = requests.get(item_url)
			url = result.json()['o:original_url']
			relative_url = url.replace("http://localhost:81/", "https://blockchain-omekas.dlll.nccu.edu.tw/")
			# print(relative_url)
			print('video link')
		elif format == "image":
			url = item['results'][0]["thumbnail_display_urls"]["square"]
			relative_url = url.replace("http://localhost:81/", "https://blockchain-omekas.dlll.nccu.edu.tw/")
			print('img link')
	return relative_url


async def test(chain, session):  # fetch SetRoom event to DB
	null_source =session.query(Asset_nft) \
		.filter(Asset_nft.source == '') \
		.all()
	for s in null_source:
		print(s.transactionHash)
		transactionHash = s.transactionHash
		NftId = s.NftId
		img = await source(transactionHash, NftId)
		# print(img)
		i = 0
		if not img:
			# 資料庫更新
			update_target = session.query(Asset_nft).filter_by(transactionHash=transactionHash).first()
			update_target.source = ''
			session.commit()
			i += 1
		else:
			update_target = session.query(Asset_nft).filter_by(transactionHash=transactionHash).first()
			update_target.source = img
			session.commit()
			i += 1

	print('%d new Nft_mint events' % i)
def main():
	# sqlalchemy init
	engine = create_engine(SQLALCHEMY_HOST_URI)
	Session = sessionmaker(bind=engine)
	session = Session()

	skychain = Web3(Web3.HTTPProvider('https://rpc.skychainnet.com'))  # set web3 target
	skychain.middleware_onion.inject(geth_poa_middleware, layer=0)


	# test(skychain, session)
	asyncio.run(test(skychain, session))



if __name__ == "__main__":
	main()