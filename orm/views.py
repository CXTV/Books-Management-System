from django.shortcuts import render,redirect
from orm import models
# Create your views here.

def index(request):
	
	bookList = models.Book.objects.all()
	return render(request,'index.html',{'bookList':bookList})

def add(request):

	if request.method == 'POST':
		title = request.POST.get('title')
		author = request.POST.get('author')
		pubDate = request.POST.get('pubdate')
		publish = request.POST.get('publish')
		book_obj = models.Book.objects.create(title=title,author=author,publishDate=pubDate,publish=publish)
		return redirect('/index/')

	return render(request,'addbook.html')

def delbook(request,id):

	models.Book.objects.filter(nid=id).delete()
	return redirect('/index/')


def editbook(request):

	if request.method == "POST":
		id = request.POST.get('book_id')
		title = request.POST.get('title')
		author = request.POST.get('author')
		date = request.POST.get('date')
		publish = request.POST.get('publish')

		models.Book.objects.filter(nid=id).update(title=title,author=author,publishDate=date,publish=publish)
		return redirect('/index/')

	id = request.GET.get('book_id')
	editbook=models.Book.objects.filter(nid=id)[0]  #    [obj1,]


	return render(request,'edit.html',{'editbook':editbook})


