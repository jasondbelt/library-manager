#RENTAL_APP.SERIALIZERS
from .models import Rental
from book_app.models import Book
from rest_framework import serializers

class RentalSerializer(serializers.ModelSerializer):
    rentals = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Rental
        fields = ["id", "rental_list", "rentals"]