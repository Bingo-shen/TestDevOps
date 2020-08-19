from django.http import HttpResponse
from django.shortcuts import reverse,redirect



def index(request):
	username = request.GET.get('username')
	if username:
		return HttpResponse('首页')
	else:
		# login_url = reverse('login')
		# return redirect(login_url)
		# article_url = reverse('article',kwargs={"article_id":1})
		# return redirect(article_url)
		login_url = reverse('login') + "?next=/"
		return redirect(login_url)

def login(request):
	return HttpResponse('登陆首页')

def article(request,article_id):
	text = '您的文章id是：%s' % article_id
	return HttpResponse(text)