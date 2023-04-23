# -*- coding: utf-8 -*-
from solid.extension import db


class Transfer(db.Model):
	__tablename__ = 'transfer'
	id = db.Column(db.Integer, primary_key=True)
	token_from = db.Column(db.String(42))
	token_to = db.Column(db.String(42))
	token_tokenId = db.Column(db.Integer)
	token_transactionHash = db.Column(db.String(66))
	token_blockNumber = db.Column(db.Integer)
