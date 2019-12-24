from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('appointment/', Appointment.as_view(), name='appointment'),
    path('staff/', Staff.as_view(), name='staff'),
    path('staff/detail/<int:id>/', StaffDetail.as_view(), name='staff_detail'),
    path('illnesses/', Illnesses.as_view(), name='illnesses'),
    path('illnesses/detail/<int:id>/', IllnessesDetail.as_view(), name='illnesses_detail'),
    path('personal/clients/', AppointmentStaff.as_view(), name='clients'),
    path('personal/clients/delete/<int:id>/', DeleteClient, name='delete_client'),
    path('personal/clients/<int:id>/visits/', Visits.as_view(), name='visits'),
    path('personal/pet/<int:id>/history/', History.as_view(), name='history'),
    path('personal/pet/<int:id>/card/', Card.as_view(), name='card'),
    path('personal/staff/statistics/', Statistics.as_view(), name='statistics'),
]