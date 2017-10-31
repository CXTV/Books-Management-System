from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from app01 import models

def index(request):

    all_book_list=models.Book.objects.all()


    return render(request,"index.html",locals())

def add(request):
    if request.method=="POST":
        title=request.POST.get("title")
        price=request.POST.get("price")
        pubDate=request.POST.get("pubDate")
        publish_id=request.POST.get("publisher")
        authors_id_list=request.POST.getlist("authorlist")

        current_book=models.Book.objects.create(title=title,price=price,publishDate=pubDate,publish_id=publish_id)
        authors=models.Author.objects.filter(id__in=authors_id_list)
        current_book.authorlist.add(*authors)
        print(request.POST)

        return redirect("/index/")
    publishList=models.Publish.objects.all()
    authorList=models.Author.objects.all()
    return render(request,"add.html",locals())


def edit(request,edit_book_id):
    edit_book=models.Book.objects.filter(id=edit_book_id).first()
    publishList = models.Publish.objects.all()
    authorList = models.Author.objects.all()
    edit_book_authors=edit_book.authorlist.all().values_list("id")
    print(edit_book_authors)
    l=[]

    for i in edit_book_authors:
        l.append(i[0])  # [2,3]
    return render(request,"edit.html",locals())