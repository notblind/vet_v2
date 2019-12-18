from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy


from django.views import generic
from .forms import SignUpForm
from django.contrib.auth.models import Group
from personal.models import *
# Create your views here.

class SignUp(generic.CreateView):
	form_class = SignUpForm
	success_url = reverse_lazy('login')
	template_name = 'accounts/signup.html'

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.save() 
		ds = DistrictModel.objects.get(id=1)
		cl = ClientModel(user=instance, district=ds, points=0)
		cl.save()
		return redirect('login')

from django.contrib.auth import logout
def LogOut(request):
	logout(request)
	return reverse_lazy('index')