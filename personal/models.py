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

class ClientModel(models.Model):
	district = models.ForeignKey(DistrictModel, on_delete=models.CASCADE)
	points = models.PositiveSmallIntegerField(default=0)
	user = models.OneToOneField(User, on_delete = models.CASCADE)

