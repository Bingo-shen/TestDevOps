from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect,reverse

def index(request):
	# 如果用户没有登陆那么让他跳转到登陆页面
	username = request.GET.get('username')
	if username:
		return HttpResponse('前台首页')
	else:
		return redirect(reverse('front:login'))


def login(request):
	return HttpResponse('前台登陆页面')