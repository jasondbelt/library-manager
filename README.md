# Django Assignment: Library Management API with DRF and PostgreSQL

In this assignment, you will create a RESTful API using Django Rest Framework (DRF) and PostgreSQL for managing a library. The API will handle books and clients, with clients being token authenticated users. Additionally, clients will have the ability to rent or return books. You will also receive a JSON fixture with 9 Book objects of 3 different genres to load into your database.

## Table of Contents:

1. Project Setup
2. Creating Models
3. Serializers and Views
4. Endpoints
7. JSON Fixture
8. Instructions



## 1. Project Setup:

1. Create a new Django project: `django-admin startproject library_management_project .`
2. Create a new app for the Library management system: `python manage.py startapp library_app`
3. Create a new app for the Client management system: `python manage.py startapp client_app`
4. Create a new app for the Book management system: `python manage.py startapp book_app`
5. Install required packages:

```bash
pip install djangorestframework
pip install "psycopg[binary]"
```

6. Configure PostgreSQL database settings in `settings.py`.
7. Configure rest_framework Token Authentication settings in `settings.py`.

```python
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'rest_framework.authtoken',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
```

8. Configure AUTH_USER_MODEL settings in settings.py

## 3. Creating Models:

Define the models for Book, Client, and Rental with appropriate fields:

```python
class Book(models.Model):
    pass

class Client(models.Model):
    pass

class Rental(models.Model):
    pass
```

## 4. Serializers and Views:

Create serializers for Book, Client, and Rental models:

```python
class BookSerializer(serializers.ModelSerializer):
    pass

class ClientSerializer(serializers.ModelSerializer):
    pass

class RentalSerializer(serializers.ModelSerializer):
    pass
```

Create views for handling the necessary APIViews to meet the requirements

## 6. Endpoints:
Define the following endpoints for the library API:

1. Books:
   - GET `/api/books/`: Retrieve a list of all books in the library. (Expected return: List of book objects)
   - GET `/api/books/{book_id}/`: Retrieve details of a specific book by its ID. (Expected return: Book object)

2. Clients:
   - GET `/api/clients/`: Retrieve details of a specific client by their ID. (Expected return: Client object)
   - POST `/api/clients/signup/`: Create a new client with token in the library. (Expected return: Created client object)
   - POST `/api/clients/login/`: Gets or creates a clients token. (Expected return: Created client object)
   - POST `api/clients/logout/`: Deletes a clients token


3. Rentals:
   - GET `/api/rentals/`: Retrieve a list of all book rentals pertaining to the user making the request. (Expected return: List of rental objects)
   - GET `/api/rentals/{rental_id}/`: Retrieve details of a specific rental by its ID. (Expected return: Rental object)
   - POST `/api/rentals/`: Create a new rental for a client to rent out a book. (Expected return: Created rental object)
   - PUT `/api/rentals/{rental_id}/`: Update details of a specific rental by its ID. (Expected return: Updated rental object)
   - DELETE `/api/rentals/{rental_id}/`: Delete a specific rental by its ID. (Expected return: HTTP 204 No Content)

## 8. Instructions:

1. Set up a new Django project and necessary apps.
2. Configure your PostgreSQL database settings in Django settings.py file.
3. Create models for Book, Client, and Rental with appropriate fields.
4. Load the provided JSON fixture into the database using a Django management command.
5. Implement serializers for Book, Client, and Rental models using Django Rest Framework serializers.
6. Create views for Book, Client, and Rental models, and add token authentication for client views.
7. Set up URL patterns to connect the views to their respective endpoints.
8. Implement appropriate view functions for each endpoint, handling GET, POST, PUT, and DELETE requests.
9. Test your API using Postman, or any API testing tool of your choice to ensure all operations work as expected.
