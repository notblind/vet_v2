from django.urls import path

from .views import *

urlpatterns = [
    path('personal/', Personal.as_view(), name='personal'),
]
