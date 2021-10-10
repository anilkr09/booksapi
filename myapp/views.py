from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import requests
import json
from myapp.models import Book
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return HttpResponse(("This is homepage"))

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



@csrf_exempt
def books(req):
   
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
        book["authors"]=[authors]
        book["number_of_pages"]=number_of_pages
        book["publisher"]=publisher
        book["country"]=country
        book["release_date"]=release_date
        data.append(book)
        response_data["data"]=data;
        
        return HttpResponse(json.dumps(response_data))
        

    response_data = {"status_code":200,"status":"success","data":[]}
    s_name=req.GET.get('name')
    s_country=req.GET.get('country')
    s_publisher=req.GET.get('publisher')
    s_releasedate=req.GET.get('release_date')
    flag=0
    if(s_name):
        flag=1
        book_info =Book.objects.filter(name=s_name).values().first()
    if(s_country):
        flag=1
        book_info =Book.objects.filter(country=s_country).values().first()
    if(s_publisher):
        flag=1
        book_info =Book.objects.filter(publisher=s_publisher).values().first()  
    if(s_releasedate):
        flag=1
        book_info =Book.objects.filter(release_date=s_releasedate).values().first()
    if(flag):
        if(book_info):
            book={}
            data=[]
            book["name"]=book_info["name"]
            book["isbn"]=book_info["isbn"]
            book["authors"]=[book_info["authors"]]
            book["number_of_pages"]=book_info["number_of_pages"]
            book["publisher"]=book_info["publisher"]
            book["country"]=book_info["country"]
            book["release_date"]=(book_info["release_date"]).strftime('%Y-%m-%d')

            data.append(book)
            response_data["data"]=data;
            return HttpResponse(json.dumps(response_data))
        else:
            response_data = {"status_code":200,"status":"success","data":[]}
            return HttpResponse(json.dumps(response_data))

    book_info =Book.objects.all().values()
    data=[]
    for o in book_info : 
        print(o)
        book={}
        book["name"]=o["name"]
        book["isbn"]=o["isbn"]
        book["authors"]=[o["authors"]]
        book["number_of_pages"]=o["number_of_pages"]
        book["publisher"]=o["publisher"]
        book["country"]=o["country"]
        book["release_date"]=(o["release_date"]).strftime('%Y-%m-%d')
        data.append(book)
       
    response_data["data"]=data;
    return HttpResponse(json.dumps(response_data))

@csrf_exempt
def bookupdate(req,bookid=1):
    
    book_object =Book.objects.filter(id=bookid).first();
    if(book_object):
        name=req.POST.get('name')
        if(name):
            book_object.name=name
        isbn=req.POST.get('isbn')
        if(isbn):
            book_object.isbn=req.POST.get('isbn')
        authors=req.POST.get('authors')
        if(authors):
            book_object.authors=req.POST.get('authors')
        country=req.POST.get('country')
        if(country):
            book_object.country=req.POST.get('country')
        number_of_pages=req.POST.get('number_of_pages')
        if(number_of_pages):
            book_object.number_of_pages=req.POST.get('number_of_pages')
        publisher=req.POST.get('publisher')
        if(publisher):
            book_object.publisher=req.POST.get('publisher')
        release_date=req.POST.get('release_date')
        if(release_date):
            book_object.release_date=req.POST.get('release_date')
        book_object.save()
    else:
        response_data = {"status_code":200,"status":"success", "message": "No book with given Id exists"}
        return HttpResponse(json.dumps(response_data))

    response_data = {"status_code":200,"status":"success", "message": "The book My First Book was updated successfully"}   
    data=[]
    book={}
    book["name"]=book_object.name
    book["isbn"]=book_object.isbn
    book["authors"]=book_object.authors
    book["number_of_pages"]=book_object.number_of_pages
    book["publisher"]=book_object.publisher
    book["country"]=book_object.country
    book["release_date"]=(book_object.release_date).strftime('%Y-%m-%d')
    data.append(book)
    response_data["data"]=data;
    return HttpResponse(json.dumps(response_data))
        
    






    

@csrf_exempt
def bookdelete(req,bookid=1):
    response_data = {"status_code":200,"status":"success","message": "The book My First Book was deleted successfully","data":[]}
    bookobject=Book.objects.filter(id=bookid).first()
    if bookobject:
        bookobject.delete()
    return HttpResponse(json.dumps(response_data));


@csrf_exempt
def book(req,bookid=1):
    response_data = {"status_code":200,"status":"success","data":[]}
    book_info =Book.objects.filter(id=bookid).values().first()
    
    if (book_info):
        book={}
        book["name"]=book_info["name"]
        book["isbn"]=book_info["isbn"]
        book["authors"]=[book_info["authors"]]
        book["number_of_pages"]=book_info["number_of_pages"]
        book["publisher"]=book_info["publisher"]
        book["country"]=book_info["country"]
        book["release_date"]=(book_info["release_date"]).strftime('%Y-%m-%d')
        response_data["data"]=[book];
    return HttpResponse(json.dumps(response_data));
