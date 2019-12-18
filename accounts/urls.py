from django.urls import path
from django.urls import include
from .views import *

urlpatterns = [
	path('', include('django.contrib.auth.urls')),
	path('signup/', SignUp.as_view(), name='signup'),
	path('logout/', LogOut, name='logout'),
]