# -*- coding: utf-8 -*-
from solid.extension import db


class Token(db.Model):
	__tablename__ = 'token'
	id = db.Column(db.Integer, primary_key=True)
	token_tokenId = db.Column(db.Integer)
	owner = db.Column(db.String(42))
	status = db.Column(db.Integer)
