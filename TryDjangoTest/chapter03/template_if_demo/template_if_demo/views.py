#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render

def index(request):
	context ={
		'age': 19
	}
	return render(request,'index.html',context=context)



