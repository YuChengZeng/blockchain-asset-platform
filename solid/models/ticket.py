# -*- coding: utf-8 -*-
from solid.extension import db

class Ticket(db.Model):
	__tablename__ = 'ticket'
	id = db.Column(db.Integer, primary_key=True)
	address = db.Column(db.String(42))
	ticket_id = db.Column(db.Integer)
	room_id = db.Column(db.String(64))
	price = db.Column(db.Integer)
	blockNumber = db.Column(db.Integer)