#CLIENT_APP.URLS
from django.urls import path
from .views import All_clients, SignUp, LogIn, LogOut

urlpatterns = [
    path('', All_clients.as_view(), name='all_clients'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', LogIn.as_view(), name='login'),
    path('logout/', LogOut.as_view(), name='logout'),
]
