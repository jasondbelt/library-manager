#RENTAL_APP.SERIALIZERS
from .models import Rental
from book_app.serializers import BookSerializer
from client_app.serializers import ClientSerializer
from rest_framework import serializers

class RentalSerializer(serializers.ModelSerializer):
    renter = ClientSerializer()
    rental = BookSerializer()

    class Meta:
        model = Rental
        fields = ["id", "renter", "rental"]