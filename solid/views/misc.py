# -*- coding: utf-8 -*-
from flask import request


def items_pagebar(total, page, items, sort_col='created', asc='1'):
	"""
	用 mysql 的話, 可以先query一次算 total,  (然後 LIMIT 等同於 skip, 不在此使用, 預先給 sql
	:param total: total number of the result records
	:param page: which page
	:param items: how many items wanted
	:return: pagebar_attr (dict)
	"""
	skip = page * items
	if skip >= total:
		skip = 0

	last = int(total / items)  # 計算最後一頁
	if total % items == 0:
		last -= 1  # 剛好整除時, 要少一頁
	if last < 0:
		last = 0
	paging_from = max(0, min(page - 4, last - 9))  # 0以上, 盡可能取 總頁數往回9頁 or 當前頁數往回4頁
	paging_to = min(last, max(9, page + 5))  # 小於最後一頁, 盡可能取 當前頁數往後5頁 or 總頁數第9頁
	misc = {
		'start': skip + 1,
		'end': skip + items,
		'page': page,
		'items': items,
		'total': total,
		'prev': max(page - 1, 0),
		'next': min(page + 1, last),
		'last': last,
		'paging_from': paging_from,
		'paging_to': paging_to,
		'sort': request.args.get('sort') or sort_col,
		'asc': request.args.get('asc') or asc
	}
	return misc


def last_page():
	return "<script>history.go(-1)</script>"
