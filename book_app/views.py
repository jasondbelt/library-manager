#BOOK_APP.VIEWS
from django.shortcuts import render, get_object_or_404
from .serializers import Book, BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST

# Create your views here.

class All_books(APIView):
    def get(self, request):
        books = Book.objects.all()
        serialized_books = BookSerializer(books, many=True)
        return Response(serialized_books.data)


class A_book(APIView):
    def get(self, request, id):
        book = get_object_or_404(Book, id=id)
        return Response(BookSerializer(book).data)