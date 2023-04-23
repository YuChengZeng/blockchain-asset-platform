# -*- coding: utf-8 -*-
from solid.extension import db

class Room_list(db.Model):
	__tablename__ = 'room_list'
	id = db.Column(db.Integer, primary_key=True)
	room_id = db.Column(db.String(64))
	coverUrl = db.Column(db.String(128))
	signboardUrl = db.Column(db.String(128))
	title = db.Column(db.String(64))
	introduction = db.Column(db.String(256))