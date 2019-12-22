from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.views import generic

from django.core.paginator import Paginator

from accounts.models import *
from personal.models import *
from .models import *
from .forms import *

# Create your views here.

class Index(generic.View):

	def get(self, request):
		return render(request, 'veterinary/index.html')

#Персонал

class Staff(generic.View):

	def get(self, request):

		dictionary = ('А','Б','В','Г','Д','Е','Ж','З','И','К','Л','М','Н','О','П','Р','С','Т','Ф','Х','Ч','Ш')
		letter = request.GET.get('letter', '')
		

		doctor_list = StaffModel.objects.all().filter(user__last_name__startswith=letter)

		paginator = Paginator(doctor_list, 9)
		page_number = request.GET.get('page', 1)
		page = paginator.get_page(page_number)

		is_paginated = page.has_other_pages()

		if page.has_previous():
			prev_url = '?page={}'.format(page.previous_page_number())
		else:
			prev_url = ''

		if page.has_next():
			next_url = '?page={}'.format(page.next_page_number())
		else:
			next_url = ''

		context = {
			'doc': page,
			'prev_url':prev_url,
			'next_url':next_url,
			'is_paginated':is_paginated,
			'dictionary': dictionary,
			'letter': letter,
		}
		return render(request, 'veterinary/staff.html', context=context)

class StaffDetail(generic.View):

	def get(self, request, id):
		doctor = StaffModel.objects.get(id=id)
		return render(request, 'veterinary/detail.html', context={'doc': doctor})

#Болезни

class Illnesses(generic.View):

	def get(self, request):
		illnesses = IllnessModel.objects.all()
		animal = AnimalModel.objects.all()
		return render(request, 'veterinary/illnesses.html', context={'illnesses': illnesses, 'animals': animal})

class IllnessesDetail(generic.View):

	def get(self, request, id):
		illness = IllnessModel.objects.get(id=id)
		return render(request, 'veterinary/detail_illness.html', context={'illness': illness})

#запись
class Appointment(generic.View):

	def get(self, request):
		check = False
		if request.user.is_authenticated:
			client = ClientModel.objects.get(user=request.user)
			try:
				animals = AnimaClientModel.objects.filter(client=client)
			except:
				animals = None
			if animals:	
				form = AppointmentRForm(client=client)
			else:
				check = True
				form=None
		else:
			form = AppointmentForm()
		return render(request, 'veterinary/appointment.html', context={'form': form, 'check': check})

	def post(self, request):
		if request.user.is_authenticated:
			client = ClientModel.objects.get(user=request.user)
			form = AppointmentRForm(request.POST, client=client,)
			if form.is_valid():
				staff = form.cleaned_data['staff']
				animal = form.cleaned_data['animal']
				date = form.cleaned_data['date']

				client = ClientModel.objects.get(user=request.user)
				appointment = AppointmentModel(staff=staff, district=client.district, date=date, animal=animal)
				appointment.save()
				return redirect('index')
		else:
			form = AppointmentForm(request.POST)
			if form.is_valid():
				staff = form.cleaned_data['staff']
				district = form.cleaned_data['district']
				date = form.cleaned_data['date']
				email = form.cleaned_data['email']

				appointment = AppointmentModel(staff=staff, district=district, date=date, email=email)
				appointment.save()
				return redirect('index')
		return redirect('index')


#Клиенты стафа
import datetime

class AppointmentStaff(generic.View):

	def get(self, request):
		form = {}
		illness = {}
		form_status = {}
		staff = StaffModel.objects.get(user=request.user)
		appointments = AppointmentModel.objects.filter(staff=staff)
		for appointment in appointments:
			if appointment.animal:
				form[appointment.id] = IllnessForm(animal=appointment.animal.animal)
			else:
				form[appointment.id] = IllnessForm(animal=None)
			try:
				illness[appointment.id] = IllnessAppointment.objects.filter(appointment=appointment)
			except:
				pass
			if illness[appointment.id]:
				for ill in illness[appointment.id]: 
					form_status[ill.id] = StatusForm(initial={ 'status': ill.status})
		context = {
			'appointments': appointments, 
			'form': form, 
			'illness': illness,
			'form_status': form_status,
		}
		return render(request, 'veterinary/clients.html', context=context)

	def post(self, request):
		id = request.GET.get('id', '')
		id2 = request.GET.get('id2', '')
		if id2:
			form = StatusForm(request.POST)
			if form.is_valid():
				status = form.cleaned_data['status']
				ill = IllnessAppointment.objects.get(id=id2)
				ill.status = status
				if status.id == 3:
					ill.date_end = datetime.datetime.now()
				ill.save()
				return redirect('clients')
		else:
			appointment = AppointmentModel.objects.get(id=id)
			if appointment.animal:
				form = IllnessForm(request.POST, animal=appointment.animal.animal)
			else:
				form = IllnessForm(request.POST, animal=None)
			if form.is_valid():
				illness = form.cleaned_data['illness']
				status = form.cleaned_data['status']
				illness_model = IllnessAppointment(illness=illness, status=status, appointment=appointment)
				illness_model.save()
				return redirect('clients')
		return redirect('clients')

class Visits(generic.View):

	def get(self, request, id):
		appointment = AppointmentModel.objects.get(id=id)
		visits = VisitModel.objects.filter(appointment=appointment)
		form = VisitForm()
		return render(request, 'veterinary/visits.html', context={'visits': visits, 'form': form, 'appointment': appointment})

	def post(self, request, id):
		appointment = AppointmentModel.objects.get(id=id)
		form = VisitForm(request.POST)
		if form.is_valid():
			note = form.cleaned_data['note']
			visit = VisitModel(note=note, appointment=appointment)
			visit.save()
			return redirect('visits', id=id)
		return redirect('visits', id=id)

def DeleteClient(request, id):
	try:
		appointment = AppointmentModel.objects.get(id=id)
	except:
		appointment = None
	if appointment:
		try:
			illness = IllnessAppointment.objects.filter(appointment=appointment)
		except:
			illness = None
		illness.delete()
		try:
			visit = VisitModel.objects.filter(appointment=appointment)
		except:
			visit = None
		visit.delete()
	appointment.delete()
	return redirect('card')	

#История питомца

class History(generic.View):

	def get(self, request, id):
		illnesses = {}
		visits = {}
		animal = AnimaClientModel.objects.get(id=id)
		try:
			appointments = AppointmentModel.objects.filter(animal=animal)
		except:
			appointments = None
		if appointments:
			for appointment in appointments:
				illnesses[appointment.id] = IllnessAppointment.objects.filter(appointment=appointment)
		context = {
			'animal': animal,
			'illnesses': illnesses,
		}
		return render(request, 'veterinary/history.html', context=context)

#Карточка питомца

class Card(generic.View):

	def get(self, request, id):
		illnesses = {}
		visits = {}
		animal = AnimaClientModel.objects.get(id=id)
		try:
			appointments = AppointmentModel.objects.filter(animal=animal)
		except:
			appointments = None
		if appointments:
			for appointment in appointments:
				illnesses[appointment.id] = IllnessAppointment.objects.filter(appointment=appointment)
				visits[appointment.id] = VisitModel.objects.filter(appointment=appointment)
		context = {
			'animal': animal,
			'appointments': appointments,
			'illnesses': illnesses,
			'visits': visits,
		}
		return render(request, 'veterinary/card.html', context=context)