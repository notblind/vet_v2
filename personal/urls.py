from django.urls import path
from django.urls import include

from .views import *

urlpatterns = [
    path('personal/', Personal.as_view(), name='personal'),
    path('personal/change/', ChangeClient.as_view(), name='change'),
    path('personal/add/', AddAnimal.as_view(), name='add_animal'),
    path('personal/pet/<int:id>/', GetAnimal.as_view(), name='get_animal'),
    path('personal/pet/<int:id>/change/', ChangeAnimal.as_view(), name='change_animal'),
    path('personal/pet/<int:id>/delete/', DeleteAnimal.as_view(), name='delete_animal'),
    path('personal/changestaff/', ChangeStaff.as_view(), name='change_staff'),
    path('ajax/load-breeds/', load_breeds, name='ajax_load_breeds'),
]
