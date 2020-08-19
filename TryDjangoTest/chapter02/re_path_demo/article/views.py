from django.http import HttpResponse


def srticle(request):
	return HttpResponse('文章首页')

def article_list(request,year):
	text = '您输入的年份是：%s' % year
	return HttpResponse(text)



