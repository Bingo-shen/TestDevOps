from django.shortcuts import render
from django.http import HttpResponse

def book(request):
	return HttpResponse('首页')

def book_detail(request,book_id):
	text = "获取这本书的id：{0}".format(book_id)
	return HttpResponse(text)

def book_list(request):
	return HttpResponse('这是列表页')