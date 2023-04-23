# -*- coding: utf-8 -*-
from solid.extension import db


class Asset_detail(db.Model):
	__tablename__ = 'asset_detail'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64))
	creator = db.Column(db.String(64))
	description = db.Column(db.String)
	subject = db.Column(db.String(64))
	transactionHash = db.Column(db.String(128))

