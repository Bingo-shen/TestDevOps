from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def movie(request):
	return HttpResponse('首页')

def movie_detail(request,movie_id):
	text = "获取这电影的id：{0}".format(movie_id)
	return HttpResponse(text)