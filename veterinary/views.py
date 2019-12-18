from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.views import generic

from .models import *

# Create your views here.

class Index(generic.View):

	def get(self, request):
		return render(request, 'veterinary/index.html')