# -*- coding: utf-8 -*-
from solid.extension import db


class Launch_to_nft(db.Model):
	__tablename__ = 'launch_to_nft'
	launch_id = db.Column(db.Integer, primary_key=True)
	tokenId = db.Column(db.Integer)
	operator = db.Column(db.String(42))
	status = db.Column(db.Integer)
	price = db.Column(db.Integer)
	blockNumber = db.Column(db.Integer)
