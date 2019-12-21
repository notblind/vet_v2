from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.views import generic

from accounts.models import *
from personal.models import *
from .models import *
from .forms import *

# Create your views here.

class Index(generic.View):

	def get(self, request):
		return render(request, 'veterinary/index.html')

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
			print(form)
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
				visit = VisitModel(appointment=appointment, date=date)
				visit.save()
				return redirect('index')
		return redirect('index')


#Клиенты стафа

class AppointmentStaff(generic.View):

	def get(self, request):
		staff = StaffModel.objects.get(user=request.user)
		appointments = AppointmentModel.objects.filter(staff=staff)
		return render(request, 'veterinary/clients.html', context={'appointments': appointments})

class Visits(generic.View):

	def get(self, request, id):
		appointment = AppointmentModel.objects.get(id=id)
		visits = VisitModel.objects.filter(appointment=appointment)
		return render(request, 'veterinary/visits.html', context={'visits': visits})