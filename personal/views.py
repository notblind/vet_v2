from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .models import *
from .forms import *
# Create your views here.


class Personal(generic.View):

	def get(self, request):
		animals = None
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
			if pers:
				try:
					animals = AnimaClientModel.objects.filter(client=pers)
				except:
					animals = None

		return render(request, 'personal/personal.html', context={'pers': pers, 'animals': animals})

#Client personal

def load_breeds(request):
	animal = request.GET.get('animal')
	breeds = BreedModel.objects.filter(animal=animal).order_by('name')
	return render(request, 'personal/city_dropdown_list_options.html', {'breeds': breeds})

class AddAnimal(generic.View):

	def get(self, request):
		form = AddAnimalForm()
		return render(request, 'personal/addanimal.html', context={'form': form})

	def post(self, request):
		form = AddAnimalForm(request.POST, request.FILES)
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

from django.contrib.auth.mixins import LoginRequiredMixin
class ChangeClient(LoginRequiredMixin, generic.View):

	def get(self, request):
		client = ClientModel.objects.get(user=request.user)
		initial = {
			'name': request.user.first_name,
			'surname': request.user.last_name,
			'middle': request.user.middle_name,
			'email': request.user.email,
			'district': client.district,
			'foto':  request.user.foto,
		}
		form = ChangeClientForm(initial=initial)
		return render(request, 'personal/change.html', context={'form': form})

	def post(self, request):
		form = ChangeClientForm(request.POST, request.FILES)
		if form.is_valid():
			name = form.cleaned_data['name']
			surname = form.cleaned_data['surname']
			middle = form.cleaned_data['middle']
			email = form.cleaned_data['email']
			district = form.cleaned_data['district']
			try:
				foto = request.FILES['foto']
			except:
				foto = None

			user_model = User.objects.get(id=request.user.id)
			user_model.first_name = name
			user_model.last_name = surname
			user_model.middle_name = middle
			user_model.email = email
			if foto:
				user_model.foto = foto
			user_model.save()
			client_model = ClientModel.objects.get(user=request.user)
			client_model.district = district
			client_model.save()
			return redirect('personal')
		return redirect('index')

#Pets personal

class GetAnimal(generic.View):

	def get(self, request, id):
		animal = AnimaClientModel.objects.get(id=id)
		return render(request, 'personal/animal.html', context={'animal': animal})

class ChangeAnimal(generic.View):

	def get(self, request, id):
		animal = AnimaClientModel.objects.get(id=id)
		initial = {
			'nickname': animal.nickname,
			'animal': animal.animal,
			'breed': animal.breed,
			'age': animal.age,
			'foto': animal.foto,
		}
		form = AddAnimalForm(initial=initial)
		return render(request, 'personal/changeanimal.html', context={'form': form, 'idan': id})

	def post(self, request, id):
		form = AddAnimalForm(request.POST, request.FILES)
		if form.is_valid():
			nickname = form.cleaned_data['nickname']
			animal = form.cleaned_data['animal']
			breed = form.cleaned_data['breed']
			age = form.cleaned_data['age']
			try:
				foto = request.FILES['foto']
			except:
				foto = None
			animal_model = AnimaClientModel.objects.get(id=id)
			animal_model.nickname = nickname
			animal_model.animal = animal
			animal_model.breed = breed
			animal_model.age = age
			if foto:
				animal_model.foto = foto
			animal_model.save()
		return redirect('get_animal', id=id)

class DeleteAnimal(generic.View):

	def get(self, request, id=None):
		try:
			animal = AnimaClientModel.objects.get(id=id)
		except:
			animal = None
		animal.delete()
		request.method = 'GET'
		return redirect('personal')	

#Doc personal

from django.contrib.auth.mixins import LoginRequiredMixin
class ChangeStaff(LoginRequiredMixin, generic.View):

	def get(self, request):
		staff = StaffModel.objects.get(user=request.user)
		initial = {
			'name': request.user.first_name,
			'surname': request.user.last_name,
			'middle': request.user.middle_name,
			'email': request.user.email,
			'education': staff.education,
			'qualification': staff.qualification,
			'description': staff.description,
			'foto':  request.user.foto,
		}
		form = ChangeStaffForm(initial=initial)
		return render(request, 'personal/change_staff.html', context={'form': form})

	def post(self, request):
		form = ChangeStaffForm(request.POST, request.FILES)
		if form.is_valid():
			name = form.cleaned_data['name']
			surname = form.cleaned_data['surname']
			middle = form.cleaned_data['middle']
			email = form.cleaned_data['email']
			education = form.cleaned_data['education']
			qualification = form.cleaned_data['qualification']
			description = form.cleaned_data['description']
			try:
				foto = request.FILES['foto']
			except:
				foto = None

			user_model = User.objects.get(id=request.user.id)
			user_model.first_name = name
			user_model.last_name = surname
			user_model.middle_name = middle
			user_model.email = email
			if foto:
				user_model.foto = foto
			user_model.save()
			staff_model = StaffModel.objects.get(user=request.user)
			staff_model.education = education
			staff_model.qualification = qualification
			staff_model.description = description
			staff_model.save()
			return redirect('personal')
		return redirect('index')