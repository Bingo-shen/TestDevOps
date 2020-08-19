from django.http import HttpResponse

books_list =[
	'三国',
	'水浒',
	'西游',
	'红楼'
]

def books(request,page=0):
	return HttpResponse(books_list[page])
