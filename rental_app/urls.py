#RENTAL_APP.URLS
from django.urls import path
from .views import All_rentals, A_rental

urlpatterns = [
    path("", All_rentals.as_view(), name='all_rentals'),
    path("rental_id/<int:id>/", A_rental.as_view(), name="a_rental"),
]