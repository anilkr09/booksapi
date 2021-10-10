from django.db import models

# Create your models here.

class Book(models.Model):
    name=models.CharField(max_length=122)
    isbn=models.CharField(max_length=122)
    authors=models.CharField(max_length=122)
    country=models.CharField(max_length=122)
    number_of_pages=models.CharField(max_length=122)
    publisher=models.CharField(max_length=122)
    release_date=models.CharField(max_length=122)

    def __str__(self):
        return self.name
