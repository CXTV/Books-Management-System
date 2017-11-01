from django.shortcuts import render,redirect
from orm import models
# Create your views here.

def index(request):	
	bookList = models.Book.objects.all()   
	return render(request,'index.html',locals())

def add(request):
	if request.method == 'POST':
		print(request.POST)   #打印方便查看
		title = request.POST.get('title')
		author = request.POST.getlist('authorlist')    #多个对象，用getlist
		pubDate = request.POST.get('pubdate')
		publish = request.POST.get('pubnamelist')
		book_obj = models.Book.objects.create(title=title,publishDate=pubDate,pubname_id=publish)
		book_obj.authors.add(*author)    #多对多添加

		return redirect('/index/')

	publishlist = models.Pubname.objects.all()
	authorList = models.Author.objects.all()
	return render(request,'addbook.html',locals())



	return render(request,'addbook.html')

def delbook(request,id):
	models.Book.objects.filter(nid=id).delete()
	return redirect('/index/')


def editbook(request,id):
	if request.method == "POST":
		print(request.POST)
		id = request.POST.get('book_id')
		title = request.POST.get('title')
		author = request.POST.getlist('authorlist')    #多个对象，用getlist
		pubDate = request.POST.get('pubdate')
		publish = request.POST.get('pubnamelist')
		book_obj = models.Book.objects.create(title=title,publishDate=pubDate,pubname_id=publish)
		book_obj.authors.add(*author) 
		return redirect('/index/')

	bookObj = models.Book.objects.get(nid = id)
	authorList = models.Author.objects.all()
	publishlist = models.Pubname.objects.all()
	print(bookObj.publishDate)
	return render(request,'edit.html',locals())


def login(request):
    if request.method == 'POST':
    	username = request.POST.get('username')
    	password = request.POST.get('password')
    	user = auth.authenticate(request, username=username, password=password)
    	if user:
        	auth.login(request, user)
        	return redirect('/index/')
    return render(request, 'login.html')


def register(request):
	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

	return render(request,'register.html')
