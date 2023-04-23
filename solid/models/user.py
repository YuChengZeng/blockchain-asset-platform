# -*- coding: utf-8 -*-
from solid.extension import db


class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	address = db.Column(db.String(42))
	email = db.Column(db.String(128))
	name = db.Column(db.String(128))
	status = db.Column(db.Integer)
	activated = db.Column(db.Integer)
	created = db.Column(db.DateTime)
	modified = db.Column(db.DateTime)





