#BOOK_APP.SERIALIZERS
from .models import Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ["id", "title", "author", "isbn", "genre", "published_date"]