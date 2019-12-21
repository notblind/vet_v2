from django.urls import path

from .views import Comments

urlpatterns = [
	path('', Comments.as_view(), name='comments')
]