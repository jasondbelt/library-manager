#RENTAL_APP.VIEWS
from django.shortcuts import render, get_object_or_404
from .serializers import Rental, RentalSerializer
from book_app.models import Book
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED, 
    HTTP_204_NO_CONTENT, 
    HTTP_400_BAD_REQUEST,
)
# Create your views here.

class All_rentals(APIView):

    def get(self, request):
        try:
            client = request.user
            serialized_rentals = RentalSerializer(client.rental_list.all(), many=True)
            return Response(serialized_rentals.data, status=HTTP_200_OK)
        except Exception:
            return Response('invalid user', status=HTTP_400_BAD_REQUEST)

        
    def post(self, request):
        try:
            # get authenticated user
            client = request.user
            # retrieve book instuance using provided rental_id
            book = Book.objects.get(id=request.data.get('rental'))
            # create new rental instance associating client with selected book
            rental_instance = Rental.objects.create(renter=client, rental=book)
            # serialize the data
            new_rental = RentalSerializer(rental_instance)
            return Response(new_rental.data, status=HTTP_201_CREATED)
        except Exception:
            return Response('invalid post', status=HTTP_400_BAD_REQUEST)


class A_rental(APIView):
    
    def get(self, request, id):
        rental = get_object_or_404(Rental, id=id)
        return Response(RentalSerializer(rental).data)
    
    def put(self, request, id):
        rental = get_object_or_404(Rental, id=id)
        updated_rental = RentalSerializer(rental, data=request.data, partial=True)
        if updated_rental.is_valid():
            updated_rental.save()
            return Response(updated_rental.data, status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        rental = get_object_or_404(Rental, id=id)
        rental.delete()
        return Response(status=HTTP_204_NO_CONTENT)