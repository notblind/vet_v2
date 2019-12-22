from django.urls import path
from django.urls import include

from .views import *

urlpatterns = [
    path('', Personal.as_view(), name='personal'),
    path('change/', ChangeClient.as_view(), name='change'),
    path('add/', AddAnimal.as_view(), name='add_animal'),
    path('pet/<int:id>/', GetAnimal.as_view(), name='get_animal'),
    path('pet/<int:id>/change/', ChangeAnimal.as_view(), name='change_animal'),
    path('pet/<int:id>/delete/', DeleteAnimal.as_view(), name='delete_animal'),
    path('changestaff/', ChangeStaff.as_view(), name='change_staff'),
    path('ajax/load-breeds/', load_breeds, name='ajax_load_breeds'),
]
