# -*- coding: utf-8 -*-
import json
from web3 import Web3

SQLALCHEMY_HOST_URI = 'mysql://db_test1:db_test1@127.0.0.1:3306/db_test1'
RPC_URI = 'https://rpc.skychainnet.com'
address_CT = '0xDd373F70124Ca94358c12ea716359605D70367e0'
address_NFT = '0xDD36A5e7FDD7e8cd5B3fC8152C65fD3cc9cFb916'
address_ART = '0xfFCab6f313E0241c472a2DDA8858cdadFe6ac0C0'
address_TT = '0x9f82926b5264dc0C05BDB1dE400962455F0f985D'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# load contract
chain = Web3(Web3.HTTPProvider(RPC_URI))  # set web3 target
with open('/root/output/' + 'CurationToken' + '.abi', 'r') as f:
	CT_abi_json = f.readline()
with open('/root/output/' + 'AssetNFT' + '.abi', 'r') as f:
	NFT_abi_json = f.readline()
with open('/root/output/' + 'AssetRental' + '.abi', 'r') as f:
	ART_abi_json = f.readline()
with open('/root/output/' + 'Tickets' + '.abi', 'r') as f:
	TT_abi_json = f.readline()

CT_abi = json.loads(CT_abi_json)
NFT_abi = json.loads(NFT_abi_json)
ART_abi = json.loads(ART_abi_json)
TT_abi = json.loads(TT_abi_json)

contract_CT = chain.eth.contract(address=address_CT, abi=CT_abi)
contract_NFT = chain.eth.contract(address=address_NFT, abi=NFT_abi)
contract_ART = chain.eth.contract(address=address_ART, abi=ART_abi)
contract_TT = chain.eth.contract(address=address_TT, abi=TT_abi)