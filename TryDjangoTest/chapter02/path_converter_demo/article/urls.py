#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
	path('',views.article),
	path('list/<cate:categories>/',views.article_list),
	path('detail/<int:article_id>/',views.article_detail,name='detail')

]