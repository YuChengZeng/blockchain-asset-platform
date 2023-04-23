# -*- coding: utf-8 -*-
import json
from datetime import datetime
import time
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from web3 import Web3
from web3.middleware import geth_poa_middleware
from web3.exceptions import TransactionNotFound
from model import *  # if for PyCharm execution, use script.model
# from config import *  # if for PyCharm execution, use script.config
import binascii


def test(chain):
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
		# print(entry['args']['NftId'], entry['args']['sha'], entry['args']['time'], entry['args']['operator'],
		# 	  entry['transactionHash'].hex(), entry['blockNumber'])
		transactionHash = str(entry['transactionHash'].hex())
		# print(transactionHash)
		# print(img)

def main():

	skychain = Web3(Web3.HTTPProvider('https://rpc.skychainnet.com'))  # set web3 target
	skychain.middleware_onion.inject(geth_poa_middleware, layer=0)


	test(skychain)



if __name__ == "__main__":
	main()