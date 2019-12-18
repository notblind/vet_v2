from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy


from django.views import generic
from .forms import SignUpForm
from django.contrib.auth.models import Group

# Create your views here.

class SignUp(generic.CreateView):
	form_class = SignUpForm
	success_url = reverse_lazy('login')
	template_name = 'veterinary/signup.html'

	def form_valid(self, form):
		instance = form.save(commit=False)
		g = Group.objects.get(name='client')
		instance.save() 
		instance.groups.add(g)
		return redirect('login')

def LogOut(request):
	logout(request)
	return reverse_lazy(main_page)