# -*- coding: utf-8 -*-
from solid.extension import db

class Set_room(db.Model):
	__tablename__ = 'set_room'
	id = db.Column(db.Integer, primary_key=True)
	address = db.Column(db.String(42))
	room_id = db.Column(db.String(64))
	price = db.Column(db.Integer)
	blockNumber = db.Column(db.Integer)
