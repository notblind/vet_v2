from django.db import models

from accounts.models import User
# Create your models here.

class StaffModel(models.Model):
	education = models.CharField(max_length=1024)
	qualification = models.CharField(max_length=512)
	description = models.CharField(max_length=2048)
	points = models.PositiveSmallIntegerField(default=0)
	user = models.OneToOneField(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.user.first_name+' '+self.user.last_name+' '+self.user.middle_name

class DistrictModel(models.Model):
	name = models.CharField(max_length=512)

	def __str__(self):
		return self.name

class ClientModel(models.Model):
	district = models.ForeignKey(DistrictModel, on_delete=models.CASCADE)
	user = models.OneToOneField(User, on_delete = models.CASCADE)


class AnimalModel(models.Model):
	name = models.CharField(max_length=256)

	def __str__(self):
		return self.name

class BreedModel(models.Model):
	name = models.CharField(max_length=256)
	animal = models.ForeignKey(AnimalModel, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class AnimaClientModel(models.Model):
	nickname = models.CharField(max_length=256, blank=True)
	age = models.PositiveSmallIntegerField(default=0, blank=True)
	foto = models.ImageField(null=True, blank=True)
	animal = models.ForeignKey(AnimalModel, on_delete=models.CASCADE)
	client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
	breed = models.ForeignKey(BreedModel, on_delete=models.CASCADE)

	def __str__(self):
		return self.nickname
