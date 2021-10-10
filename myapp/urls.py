# URL configurations
from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
  path("",views.index,name="home"),
  path("api/external-books/",views.externalapi,name="external"),
  path("api/v1/books/<int:bookid>/",views.book,name='book'),
  path("api/v1/books/",views.books),
  path("api/v1/books/<int:bookid>/update",views.bookupdate),
  path("api/v1/books/<int:bookid>/delete",views.bookdelete)


]

