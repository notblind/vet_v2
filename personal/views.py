from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .models import *
from .forms import *
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

def load_breeds(request):
	animal = request.GET.get('animal')
	breeds = BreedModel.objects.filter(animal=animal).order_by('name')
	return render(request, 'personal/city_dropdown_list_options.html', {'breeds': breeds})

class AddAnimal(generic.View):

	def get(self, request):
		form = AddAnimalForm()
		return render(request, 'personal/addanimal.html', context={'form': form})

	def post(self, request):
		form = AddAnimalForm(request.POST)
		if form.is_valid():
			nickname = form.cleaned_data['nickname']
			animal = form.cleaned_data['animal']
			breed = form.cleaned_data['breed']
			age = form.cleaned_data['age']
			try:
				foto = request.FILES['foto']
			except:
				foto = None
			client = ClientModel.objects.get(user=request.user)
			model = AnimaClientModel(nickname=nickname,age=age,
				foto=foto,animal=animal,client=client,
				breed=breed)
			model.save()
		return redirect('personal')
