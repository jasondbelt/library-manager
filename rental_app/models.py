#RENTAL_APP.MODELS
from django.db import models
from client_app.models import Client
from book_app.models import Book

# Create your models here.
class Rental(models.Model):
    renter = models.ForeignKey(Client, on_delete=models.CASCADE)
    rentals = models.ManyToManyField(Book, related_name='books', blank=True)