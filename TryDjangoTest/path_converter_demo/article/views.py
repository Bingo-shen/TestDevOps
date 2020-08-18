from django.http import HttpResponse
from django.shortcuts import reverse



def article(request):
	return HttpResponse('文章首页')

def article_list(request,categories):
	text = '文章的类别是 %s' % categories
	return HttpResponse(text)

def article_detail(request,article_id):
	reverse('detail',kwargs={"article_id":article_id})
	return HttpResponse('文章详情')