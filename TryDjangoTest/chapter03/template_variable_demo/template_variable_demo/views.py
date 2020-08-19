#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render

class Person(object):

	def __init__(self,username):
		self.username = username



def index(request):
	p = Person('shenqiang')
	context = {
		'person':{
			'username':'shenqiang'
		}
	}
	return render(request,'index.html',context=context)