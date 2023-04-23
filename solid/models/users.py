# -*- coding: utf-8 -*-
from solid.extension import db


class Users(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(128))
	password = db.Column(db.String(40))
	name = db.Column(db.String(128))
