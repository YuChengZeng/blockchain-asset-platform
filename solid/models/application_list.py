# -*- coding: utf-8 -*-
from solid.extension import db


class Application_list(db.Model):
	__tablename__ = 'application_list'
	id = db.Column(db.Integer, primary_key=True)
	operator = db.Column(db.String(42))
	licenseId = db.Column(db.Integer)
	launchId = db.Column(db.Integer)
	price = db.Column(db.Integer)
	blockNumber = db.Column(db.Integer)