# Library Manager:

[https://github.com/Code-Platoon-Assignments/library-manager](https://github.com/Code-Platoon-Assignments/library-manager)

# Installations/Setup:

```python
# creating/activating venv
python -m venv .venv
source .venv/bin/activate
  
# installations (modify as needed)
pip install django
pip install --upgrade pip
pip install "psycopg[binary]"
pip install djangorestframework
pip install requests
pip install requests_oauthlib
pip install python-dotenv
pip freeze > requirements.txt
  
# creating database/dropping database
dropdb library_management_db && createdb library_management_db
  
# creating Project/Apps
django-admin startproject library_management_project .
python manage.py startapp rental_app
python manage.py startapp client_app
python manage.py startapp book_app

# configure settings.py (modify as needed)
INSTALLED_APPS = [
    "....",
    "rental_app",
    "client_app",
    "book_app",
    "rest_framework",
    "rest_framework.authtoken",
    "..."
  ]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'library_management_db',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

# Configure AUTH_USER_MODEL settings in settings.py
AUTH_USER_MODEL = 'client_app.Client'

#.env (modify as needed)
API_KEY=****
API_SECRET=****
# copied from settings.py
DJANGO_SECRET_KEY='****'

#.gitignore
# Ignore all .env files anywhere in the project
**/.env
# Ignore all .venv directories anywhere in the project
**/.venv/
# Ignore all __pycache__ directories anywhere in the project
**/__pycache__/

#library_management_project.urls (modify as needed)
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to the API!"})

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/books/', include('book_app.urls')),
    path('api/clients/', include('client_app.urls')),
    path('api/rentals/', include('rental_app.urls'))
]

# create 'fixtures' directories within apps, save .json files as necessary.
```

# Create models for Book, Client, and Rental with appropriate fields/ Load the provided JSON fixture into the database using a Django management command.

```python
#CLIENT_APP.MODELS
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Client(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        blank=False
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    

#BOOK_APP.MODELS
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    author = models.CharField(max_length=255, null=False, blank=False)
    isbn = models.CharField(max_length=255, null=False, blank=False)
    genre = models.CharField(max_length=255, null=False, blank=False)
    published_date = models.DateField()
    
    
#RENTAL_APP.MODELS
from django.db import models
from client_app.models import Client
from book_app.models import Book

# Create your models here.
class Rental(models.Model):
    renter = models.ForeignKey(Client, on_delete=models.CASCADE, 
        related_name='rental_list')
    rental = models.ForeignKey(Book, on_delete=models.CASCADE, 
        related_name='book')
    description = models.CharField(default="add_description", max_length=255, 
        null=False, blank=False)
        
python manage.py loaddata books.json
```

# Implement serializers for Book, Client, and Rental models using Django Rest Framework serializers.

```python
#CLIENT_APP.SERIALIZERS
from .models import Client
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ["id", "email"]
        
        
#BOOK_APP.SERIALIZERS
from .models import Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ["id", "title", "author", "isbn", "genre", "published_date"]

#RENTAL_APP.SERIALIZERS
from rest_framework import serializers
from .models import Rental
from book_app.serializers import BookSerializer
from client_app.serializers import ClientSerializer

class RentalSerializer(serializers.ModelSerializer):
    # Read (Retrieve rentals) -> Nested objects
    renter = ClientSerializer()
    rental = BookSerializer()

    class Meta:
        model = Rental
        fields = ["id", "renter", "rental", "description"]
```

# Book App Urls & Views (): 

```python
#BOOK_APP.URLS
from django.urls import path
from .views import All_books, A_book

urlpatterns = [
    path("", All_books.as_view(), name='all_books'),
    path("book_id/<int:id>/", A_book.as_view(), name="a_book"),
]

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

```

# Client App Urls & Views (): 

```python
#CLIENT_APP.URLS
from django.urls import path
from .views import All_clients, SignUp, LogIn, LogOut

urlpatterns = [
    path('', All_clients.as_view(), name='all_clients'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', LogIn.as_view(), name='login'),
    path('logout/', LogOut.as_view(), name='logout'),
]

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

```

# Rental App Urls & Views (hardest):

```python
#RENTAL_APP.URLS
from django.urls import path
from .views import All_rentals, A_rental

urlpatterns = [
    path("", All_rentals.as_view(), name='all_rentals'),
    path("rental_id/<int:id>/", A_rental.as_view(), name="a_rental"),
]

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
```