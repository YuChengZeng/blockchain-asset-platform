# -*- coding: utf-8 -*-
from solid.extension import db

class Interact(db.Model):
	__tablename__ = 'interact'
	id = db.Column(db.Integer, primary_key=True)
	address = db.Column(db.String(42))
	room_id = db.Column(db.String(64))
	target = db.Column(db.String(128))
	interact = db.Column(db.String(32))
	status = db.Column(db.Integer)