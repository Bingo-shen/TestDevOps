#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import re_path
from . import views

urlpatterns = [
	# r'',代表的是原生字符串（raw）
	re_path(r'^$',views.srticle),
	# /article/list/<year>/
	re_path(r"^list/(?P<year>\d{4})/$",views.article_list)
]


        




