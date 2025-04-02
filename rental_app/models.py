#RENTAL_APP.MODELS
from django.db import models
from client_app.models import Client
from book_app.models import Book

# Create your models here.
class Rental(models.Model):
    rental_list = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client')
    rentals = models.ManyToManyField(Book, blank=True, related_name='books')