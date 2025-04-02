#RENTAL_APP.VIEWS
from django.shortcuts import render, get_object_or_404
from .serializers import Rental, RentalSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED, 
    HTTP_204_NO_CONTENT, 
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)
# Create your views here.

class All_rentals(APIView):

    def get(self, request):
        rentals = Rental.objects.all()
        serialized_rentals = RentalSerializer(rentals, many=True)
        return Response(serialized_rentals.data)
    
    def post(self, request):
        pass


class A_rental(APIView):
    
    def get(self, request, id):
        rental = get_object_or_404(Rental, id=id)
        return Response(RentalSerializer(rental).data)
    
    def put(self, request):
        pass

    def delete(self, request):
        pass
