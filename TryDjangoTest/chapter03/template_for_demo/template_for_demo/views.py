#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render

def index(request):
	context = {
		'books' :[
			{
				'name':'三国演绎',
				'author':'罗贯中',
				'price':199
			},
			{
				'name':'水浒传',
				'author':'施耐庵',
				'price':100
			},
			{
				'name':'西游记',
				'author':'吴承恩',
				'price':89
			},
			{
				'name':'红楼梦',
				'author':'曹雪芹',
				'price':100
			}
		]
		,
		'person':
			{
				'username':'shenqiang',
				'age':18,
				'address':'nanjing'
			},
		'tests':[

		],
		'persons':[
			'张三',
			'李四',
			'王五'
		]
	}
	return render(request,'index.html',context=context)
