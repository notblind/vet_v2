from django.shortcuts import render
from django.views import generic

from .models import *

# Create your views here.
class Personal(generic.View):

	def get(self, request):
		if request.user.is_staff:
			try:
				pers = StaffModel.objects.get(user=request.user)
			except:
				pers = None
		else:
			try:
				pers = ClientModel.objects.get(user=request.user)
			except:
				pers = None
		return render(request, 'personal/personal.html', context={'pers': pers})