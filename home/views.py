from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import requests
import json
from home.models import Book

# Create your views here.

def index(request):
    return HttpResponse(("this is homepage"))

def externalapi(req):
    name=req.GET.get('name')

    r = requests.get('https://www.anapioficeandfire.com/api/books?name='+name+'')
    response_data = {"status_code":200,"status":"success","data":[]}
   
    if (r.json()):
        resp = r.json()[0];
        ress={}
        ress["name"]=resp["name"];
        ress["isbn"]=resp["isbn"]
        ress["authors"]=resp["authors"]
        ress["number_of_pages"]=resp['numberOfPages'];
        ress["publisher"]=resp["publisher"]
        ress["country"]=resp["country"]
        ress["release_date"]=(resp["released"])[:10]
        response_data["data"]=[ress];
    return JsonResponse(response_data)


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def books(req,bookid=1):
   
    if  req.method =="POST":
        name=req.POST.get('name')
        isbn=req.POST.get('isbn')
        authors=req.POST.get('authors')
        country=req.POST.get('country')
        number_of_pages=req.POST.get('number_of_pages')
        publisher=req.POST.get('publisher')
        release_date=req.POST.get('release_date')
        book=Book(name=name,isbn=isbn,authors=authors,country=country,number_of_pages=number_of_pages,
        publisher=publisher,release_date=release_date)
        book.save()
        response_data = {"status_code":200,"status":"success","data":[]}
        
        data=[]
        book={}
        book["name"]=name
        book["isbn"]=isbn
        book["authors"]=authors
        book["number_of_pages"]=number_of_pages
        book["publisher"]=publisher
        book["country"]=country
        book["release_date"]=release_date
        data.append(book)
        response_data["data"]=data;
        
        return HttpResponse(json.dumps(response_data))
        

    response_data = {"status_code":200,"status":"success","data":[]}

    a=book_info =Book.objects.all().values()
   
    data=[]
    for o in a : 
        print(o)
        book={}
        book["name"]=o["name"]
        book["isbn"]=o["isbn"]
        book["authors"]=o["authors"]
        book["number_of_pages"]=o["number_of_pages"]
        book["publisher"]=o["publisher"]
        book["country"]=o["country"]
        book["release_date"]=o["release_date"]
        data.append(book)
       
    response_data["data"]=data;
    return HttpResponse(json.dumps(response_data))


def bookupdate(req,bookid=1):
    print(bookid)
    book_object =Book.objects.filter(id=bookid).first();
    book_object.name=req.POST.get('name')
    book_object.isbn=req.POST.get('isbn')
    book_object.authors=req.POST.get('authors')
    book_object.country=req.POST.get('country')
    book_object.number_of_pages=req.POST.get('number_of_pages')
    book_object.publisher=req.POST.get('publisher')
    book_object.release_date=req.POST.get('release_date')
    bookobject.save()
    print(bookobject)

    return ;


def bookdelete(req,bookid=1):
    response_data = {"status_code":200,"status":"success","message": "The book My First Book was deleted successfully","data":[]}
    bookobject=Book.objects.filter(id=bookid).first()
    if bookobject:
        bookobject.delete()
    return HttpResponse(json.dumps(response_data));


@csrf_exempt
def book(req,bookid=1):
    response_data = {"status_code":200,"status":"success","data":[]}
    resp=book_info =Book.objects.filter(id=bookid).values().first()
    
    if (book_info):
        ress={}
        ress["name"]=resp["name"]
        ress["isbn"]=resp["isbn"]
        ress["authors"]=resp["authors"]
        ress["number_of_pages"]=resp["number_of_pages"]
        ress["publisher"]=resp["publisher"]
        ress["country"]=resp["country"]
        ress["release_date"]=resp["release_date"]
        response_data["data"]=[ress];
    return HttpResponse(json.dumps(response_data));
