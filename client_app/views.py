# #CLIENT_APP.VIEWS
# from django.shortcuts import render
# from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from .models import Client
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK, 
    HTTP_201_CREATED, 
    HTTP_204_NO_CONTENT, 
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class SignUp():
    pass

class LogIn():
    pass

class LogOut():
    pass
