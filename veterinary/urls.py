from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('appointment/', Appointment.as_view(), name='appointment'),
    path('personal/clients', AppointmentStaff.as_view(), name='clients'),
    path('personal/clients/<int:id>/visits/', Visits.as_view(), name='visits'),
]