# -*- coding: utf-8 -*-
from datetime import datetime
from flask import Blueprint, render_template, jsonify, redirect, url_for, request, g, session, flash
from re import escape
from sqlalchemy.exc import SQLAlchemyError
from solid.extension import db
from solid.views.misc import items_pagebar, last_page
from solid.models.users import Users
from solid.models.digital_objects import Digital_objects

mod = Blueprint('object_data', __name__)


def list_core(page=0, items=10):
	objects = db.session.query(Digital_objects)  # 不過濾
	total = objects.count()

	start = page * items
	if start >= total:
		start = 0
	end = start + items
	if end >= total:
		end = total

	if 'sort' in request.args and 'asc' in request.args:  # 檢查是否同時提供排序的目標欄位及排序方法
		if request.args.get('sort') in Digital_objects.__dict__.keys():
			sort_target = getattr(Digital_objects, request.args.get('sort'))
		if request.args.get('asc') == '0':  # 表示不要asc, 即desc
			objects = objects.order_by(sort_target.desc())
		else:  # 表示要asc
			objects = objects.order_by(sort_target)
	else:
		objects = objects.order_by(Digital_objects.obj_id.desc())
	objects = objects[start:end]

	misc = items_pagebar(total, page, items, 'obj_id', 0)  # 計算pagebar需要之參數
	return objects, misc


def search_core(page=0, items=10, my=False):
	objects = Digital_objects.query  # 不過濾
	if request.method == 'POST' and request.form['s_key'] and request.form['s_value']:
		session['s_key'] = request.form['s_key']
		session['s_value'] = request.form['s_value']

	if session['s_key'] == '' or session['s_value'] == '':
		redirect(url_for('object_data.simple_list'))

	search_target = getattr(Digital_objects, session['s_key'])
	objects = db.session.query(Digital_objects).filter(search_target.like('%' + session['s_value'] + '%'))

	total = objects.count()
	start = page * items
	if start >= total:
		start = 0
	end = start + items
	if end >= total:
		end = total
	if 'sort' in request.args and 'asc' in request.args:  # 檢查是否同時提供排序的目標欄位及排序方法
		if request.args.get('sort') in Digital_objects.__dict__.keys():
			sort_target = getattr(Digital_objects, request.args.get('sort'))
		if request.args.get('asc') == '0':  # 表示不要asc, 即desc
			objects = objects.order_by(sort_target.desc())
		else:  # 表示要asc
			objects = objects.order_by(sort_target)
	else:
		objects = objects.order_by(Digital_objects.obj_id.desc())
	objects = objects[start:end]

	misc = items_pagebar(total, page, items, 'obj_id', 0)  # 計算pagebar需要之參數
	misc['s_key'] = session['s_key'] or u''
	misc['s_value'] = session['s_value'] or u''
	return objects, misc


@mod.route('/search', methods=['GET', 'POST'])
@mod.route('/search/<int:page>/<int:items>', methods=['GET', 'POST'])
def search(page=0, items=10):
	"""加入搜尋條件的 manager 列表
	"""
	objects, misc = search_core(page, items)
	return render_template('object_data/list.html', objects=objects, misc=misc, action='search')


@mod.route('/')
@mod.route('/simple_list', methods=['GET', 'POST'])
@mod.route('/simple_list/<int:page>/<int:items>', methods=['GET', 'POST'])
def simple_list(page=0, items=10):
	objects, misc = list_core(page, items)
	return render_template('object_data/list.html', objects=objects, misc=misc, action='simple_list')


@mod.route('/view/<obj_id>')
def view(obj_id):
	"""顯示某筆field的頁面與細節
	"""
	object = db.session.query(Digital_objects).filter_by(obj_id=obj_id).first()

	return render_template('object_data/view.html', object=object)


@mod.route('/create', methods=['GET', 'POST'])
def create():
	"""新增一筆player資料
	"""
	if request.method == 'POST':
		new_obj = Digital_objects(
			obj_name=request.form['obj_name'],
			user_id=request.form['user_id'],
			created=datetime.utcnow()
		)
		db.session.add(new_obj)

		try:
			db.session.commit()
		except SQLAlchemyError:
			flash('create object failed', 'error')
			return last_page()

		return redirect(url_for('object_data.simple_list'))
	else:
		return render_template('object_data/create.html')


@mod.route('/update/<obj_id>', methods=['GET', 'POST'])
def update(obj_id):
	"""修改一筆player資料
	若有post則修改後更新db
	無post則查出player並顯示修改頁
	"""
	target = Digital_objects.query.filter_by(obj_id=obj_id).first()

	if request.method == 'POST':
		target.obj_name = request.form['obj_name']
		target.user_id = request.form['user_id']
		session['obj_name'] = request.form['obj_name']  # 即時更新頁面
		session['user_id'] = request.form['user_id']  # 即時更新頁面
		db.session.commit()

		return redirect(url_for('object_data.view', obj_id=obj_id))
	else:
		return render_template('object_data/update.html', object=target)


@mod.route('/delete/<obj_id>', methods=['GET', 'POST'])
def delete(obj_id):
	"""刪除某筆field資料後,回到列表頁,或著只是將status改為False
	"""
	print((obj_id))

	db.session.query(Digital_objects).filter_by(obj_id=obj_id).delete()
	db.session.commit()
	return redirect(url_for('object_data.simple_list'))
