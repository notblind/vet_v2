from django import forms

from .models import *

class AddAnimalForm(forms.ModelForm):

	nickname = forms.CharField(label='Кличка', max_length=256, required=False)
	animal = forms.ModelChoiceField(label='Выберите животное', queryset=AnimalModel.objects.all())
	breed = forms.ModelChoiceField(label='Выберите породу', queryset=BreedModel.objects.all())
	age = forms.IntegerField(label='Возраст', required=False)
	foto = forms.ImageField(label='Фото', required=False)

	class Meta:
		model = AnimaClientModel
		fields = ('nickname', 'animal', 'breed', 'age', 'foto')

	nickname.widget.attrs.update({'class':'form-control', 'placeholder':'Кличка'})
	animal.widget.attrs.update({'class':'form-control'})
	breed.widget.attrs.update({'class':'form-control'})
	age.widget.attrs.update({'class':'form-control', 'placeholder':'Возраст'})

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['breed'].queryset = BreedModel.objects.none()
		if 'animal' in self.data:
			try:
				animal_id = int(self.data.get('animal'))
				self.fields['breed'].queryset = BreedModel.objects.filter(animal=animal_id).order_by('name')
			except (ValueError, TypeError):
				pass  
		elif self.instance.pk:
			self.fields['breed'].queryset = self.instance.animal.breed_set.order_by('name')