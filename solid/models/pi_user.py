# -*- coding: utf-8 -*-
from solid.extension import db

class Pi_user(db.Model):
	__tablename__ = 'pi_user'
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(256))
	account = db.Column(db.String(256))
	password = db.Column(db.String(256))
	token = db.Column(db.String(512))
	_id = db.Column(db.String(128))
	email = db.Column(db.String(128))
	address = db.Column(db.String(42))