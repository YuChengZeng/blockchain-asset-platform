# -*- coding: utf-8 -*-
from solid.extension import db


class Digital_objects(db.Model):
	__tablename__ = 'digital_objects'
	id = db.Column(db.Integer, primary_key=True)
	hash = db.Column(db.Integer)
	obj_id = db.Column(db.Integer)
