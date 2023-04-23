# -*- coding: utf-8 -*-
from solid.extension import db


class Asset_nft(db.Model):
	__tablename__ = 'asset_nft'
	NftId = db.Column(db.Integer, primary_key=True)
	sha = db.Column(db.String(256))
	time = db.Column(db.Integer)
	operator = db.Column(db.String(42))
	transactionHash = db.Column(db.String(128))
	blockNumber = db.Column(db.Integer)
	img = db.Column(db.String(128))
