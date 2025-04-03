#RENTAL_APP.SERIALIZERS
from rest_framework import serializers
from .models import Rental
from book_app.models import Book
from client_app.models import Client
from book_app.serializers import BookSerializer
from client_app.serializers import ClientSerializer

class RentalSerializer(serializers.ModelSerializer):
    # Read (Retrieve rentals) -> Nested objects
    renter = ClientSerializer()
    rental = BookSerializer()

    class Meta:
        model = Rental
        fields = ["id", "renter", "rental"]


