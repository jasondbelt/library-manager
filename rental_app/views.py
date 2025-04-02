#RENTAL_APP.VIEWS
from django.shortcuts import render, get_object_or_404
from .serializers import Rental, RentalSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED, 
    HTTP_204_NO_CONTENT, 
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)
# Create your views here.

class All_rentals(APIView):

    def get(self, request):
        try:
            client = request.user
            all_rentals = RentalSerializer(client.rental_list.all(), many=True)
            return Response(all_rentals.data, status=HTTP_200_OK)
        except Exception as e:
            return Response(e, status=HTTP_400_BAD_REQUEST)

    
    def post(self, request):
        pass
        # data = request.data.copy()
        # data['rental_list'] = request.user.id

        # new_rental= RentalSerializer(data=data, partial=True)

        # if new_rental.is_valid():
        #     new_rental.save()
        #     new_rental.rentals.set(request.data.get('rentals', []))
        #     return Response(new_rental.data, status=HTTP_201_CREATED)
        # return Response(new_rental.errors, status=HTTP_400_BAD_REQUEST)



class A_rental(APIView):
    
    def get(self, request, id):
        rental = get_object_or_404(Rental, id=id)
        return Response(RentalSerializer(rental).data)
    
    def put(self, request):
        pass

    def delete(self, request):
        pass
