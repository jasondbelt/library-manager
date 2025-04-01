from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    author = models.CharField(max_length=255, null=False, blank=False)
    isbn = models.CharField(max_length=255, null=False, blank=False)
    genre = models.CharField(max_length=255, null=False, blank=False)
    published_date = models.DateField()
    
    
    