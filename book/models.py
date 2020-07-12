from django.db import models
from django.utils import timezone 

# Create your models here.

# this is the author class 
class Author(models.Model):
	first_name = models.CharField(max_length = 200)
	last_name = models.CharField(max_length = 200)
	place_of_birth = models.CharField(max_length = 200, )
	date_of_birth = models.DateTimeField(blank = True, null = True)
	date_of_death = models.DateTimeField(blank = True, null = True)


	

class Publisher(models.Model):
	name_of_publisher = models.CharField(max_length= 200)
	location_of_publisher = models.CharField(max_length = 200)
	date_of_creation = models.DateTimeField(blank = True, null = True)

class Book(models.Model):
    book_title = models.CharField(max_length = 200)
    author = models.ForeignKey(Author, on_delete = models.SET_NULL, null = True)
    published_by = models.ForeignKey(Publisher, on_delete = models.SET_NULL, null = True)
    date_published = models.DateTimeField(blank = True, null = True)


    	