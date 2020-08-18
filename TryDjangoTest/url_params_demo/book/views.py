# Create your views here.
from django.http import HttpResponse

def book(request):
	return HttpResponse("图书首页")

def book_detil(request,book_id,catgroy_id):
	# 从数据库中根据book_id获取图书信息
	txt = "从数据库中获取书本的id为:{0},编号为{1}".format(book_id,catgroy_id)
	return HttpResponse(txt)

def author_detail(request):
	authorid = request.GET.get('id')
	text = "作者ID是：{0}".format(authorid)
	return HttpResponse(text)

def publisher_detail(request,publisher_id):
	text = "出版社的id：{0}".format(publisher_id)
	return HttpResponse(text)