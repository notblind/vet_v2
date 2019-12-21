from django import forms

from .models import *

class AddAnimalForm(forms.ModelForm):

	nickname = forms.CharField(label='Кличка', max_length=256, required=False)
	animal = forms.ModelChoiceField(label='Выберите животное', queryset=AnimalModel.objects.all())
	breed = forms.ModelChoiceField(label='Выберите породу', queryset=BreedModel.objects.all())
	age = forms.IntegerField(label='Кол-во полных лет')
	foto = forms.ImageField(label='Фото', required=False)

	class Meta:
		model = AnimaClientModel
		fields = ('nickname', 'animal', 'breed', 'age', 'foto')

	nickname.widget.attrs.update({'class':'form-control', 'placeholder':'Кличка'})
	animal.widget.attrs.update({'class':'form-control'})
	breed.widget.attrs.update({'class':'form-control'})
	age.widget.attrs.update({'class':'form-control', 'placeholder':'Кол-во полных лет'})

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		#self.fields['breed'].queryset = BreedModel.objects.none()
		if 'animal' in self.data:
			try:
				animal_id = int(self.data.get('animal'))
				self.fields['breed'].queryset = BreedModel.objects.filter(animal=animal_id).order_by('name')
			except (ValueError, TypeError):
				pass  
		elif self.instance.pk:
			self.fields['breed'].queryset = self.instance.animal.breed_set.order_by('name')

class ChangeClientForm(forms.Form):
	name = forms.CharField(label='Имя', max_length=256, required=False)
	surname = forms.CharField(label='Фамилия', max_length=256, required=False)
	middle = forms.CharField(label='Отчество', max_length=256, required=False)
	email = forms.EmailField(label='Почта', max_length=256, required=False)
	district = forms.ModelChoiceField(label='Район', queryset=DistrictModel.objects.all(), required=False)
	foto = forms.FileField(label='Фото',required=False)

	name.widget.attrs.update({'class':'form-control', 'placeholder':'Имя'})
	surname.widget.attrs.update({'class':'form-control', 'placeholder':'Фамилия'})
	middle.widget.attrs.update({'class':'form-control', 'placeholder':'Отчество'})
	email.widget.attrs.update({'class':'form-control', 'placeholder':'Почта'})
	district.widget.attrs.update({'class':'form-control', 'placeholder':'Район'})

class ChangeStaffForm(forms.Form):
	name = forms.CharField(label='Имя', max_length=256)
	surname = forms.CharField(label='Фамилия', max_length=256)
	middle = forms.CharField(label='Отчество', max_length=256)
	email = forms.EmailField(label='Почта', max_length=256)
	education = forms.CharField(label='Образование', max_length=1024)
	qualification = forms.CharField(label='Квалификация', max_length=512)
	description = forms.CharField(label='Описание', max_length=2048)
	foto = forms.FileField(label='Фото')

	name.widget.attrs.update({'class':'form-control', 'placeholder':'Имя'})
	surname.widget.attrs.update({'class':'form-control', 'placeholder':'Фамилия'})
	middle.widget.attrs.update({'class':'form-control', 'placeholder':'Отчество'})
	email.widget.attrs.update({'class':'form-control', 'placeholder':'Почта'})
	education.widget.attrs.update({'class':'form-control', 'placeholder':'Образование'})
	qualification.widget.attrs.update({'class':'form-control', 'placeholder':'Квалификация'})
	description.widget.attrs.update({'class':'form-control', 'placeholder':'Описание'})