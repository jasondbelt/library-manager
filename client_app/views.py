# #CLIENT_APP.VIEWS
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED, 
    HTTP_204_NO_CONTENT, 
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Client
from client_app.serializers import ClientSerializer


class TokenReq(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


# Create your views here.

class All_clients(APIView):

    def get(self, request):
        clients = Client.objects.all()
        serialized_clients = ClientSerializer(clients, many=True)
        return Response(serialized_clients.data)


class SignUp(APIView):
    """
    dummy data requires email and password
    {
        "email": "jason@example.com",
        "password" : "123"
    }
        "token": "48650dfaa4d7e926a56a8728c4aa414991b0683f"
   """
    def post(self, request):
        data = request.data.copy()
        data['username'] = data['email']
        new_client = Client.objects.create_user(**data)
        if new_client:
            token = Token.objects.create(user=new_client)
            return Response({"client": new_client.email, "token": token.key}, status=HTTP_201_CREATED)
        return Response("Invalid client credentials", status=HTTP_400_BAD_REQUEST)


class LogIn(APIView):
    
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        client = authenticate(username=email, password=password)
        if client:
            token, created = Token.objects.get_or_create(user=client)
            return Response({"token": token.key, "client": client.email})
        else:
            return Response("No client matching credentials", status=HTTP_404_NOT_FOUND)


class LogOut(TokenReq):
    
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=HTTP_204_NO_CONTENT)