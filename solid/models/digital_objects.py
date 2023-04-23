# -*- coding: utf-8 -*-
from solid.extension import db


class Digital_objects(db.Model):
	__tablename__ = 'digital_objects'
	obj_id = db.Column(db.Integer, primary_key=True)
	obj_name = db.Column(db.String(42))
	user_id = db.Column(db.Integer)
	created = db.Column(db.DateTime)
