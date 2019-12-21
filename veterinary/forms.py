from django import forms

from .models import *
from personal.models import *

import datetime

class DateInput(forms.DateInput):
	input_type = 'date'

class AppointmentForm(forms.Form):
	staff = forms.ModelChoiceField(label='Выберите специалиста', queryset=StaffModel.objects.all())
	district = forms.ModelChoiceField(label='Выберите ваш район', queryset=DistrictModel.objects.all())
	email = forms.EmailField(max_length=256) 
	date = forms.DateField(widget=DateInput)

	staff.widget.attrs.update({'class':'form-control'})
	district.widget.attrs.update({'class':'form-control'})
	email.widget.attrs.update({'class':'form-control'})
	date.widget.attrs.update({'class':'form-control'})

class AppointmentRForm(forms.Form):
	animal = forms.ModelChoiceField(label='Выберите питомца', queryset=None)
	def __init__(self, *args, **kwargs):

		client = kwargs.pop('client', None)
		super(AppointmentRForm, self).__init__(*args, **kwargs)
		self.fields['animal'].queryset = AnimaClientModel.objects.filter(client=client)
	
	staff = forms.ModelChoiceField(label='Выберите специалиста', queryset=StaffModel.objects.all())
	date = forms.DateField(widget=DateInput)

	staff.widget.attrs.update({'class':'form-control'})
	animal.widget.attrs.update({'class':'form-control'})
	date.widget.attrs.update({'class':'form-control'})



