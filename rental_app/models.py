#RENTAL_APP.MODELS
from django.db import models
from client_app.models import Client
from book_app.models import Book

# Create your models here.
class Rental(models.Model):
    renter = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='rental_list')
    rental = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book')
    description = models.CharField(default="add_description", max_length=255, null=False, blank=False)