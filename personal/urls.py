from django.urls import path
from django.urls import include

from .views import *

urlpatterns = [
    path('personal/', Personal.as_view(), name='personal'),
    path('add/animal/', AddAnimal.as_view(), name='add_animal'),
    path('ajax/load-breeds/', load_breeds, name='ajax_load_breeds'),
]
