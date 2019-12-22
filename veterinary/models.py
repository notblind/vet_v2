from django.db import models

from accounts.models import *
from personal.models import *
# Create your models here.


class IllnessModel(models.Model):
	name = models.CharField(max_length=256)
	description = models.CharField(max_length=1024)
	animal = models.ForeignKey(AnimalModel, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class AppointmentModel(models.Model):
	date = models.DateField()
	staff = models.ForeignKey(StaffModel, on_delete=models.CASCADE)
	animal = models.ForeignKey(AnimaClientModel, on_delete=models.CASCADE, blank=True, null=True)
	district = models.ForeignKey(DistrictModel, on_delete=models.CASCADE)
	email = models.EmailField(max_length=256, unique=False, blank=True, null=True)

class StatusModel(models.Model):
	name = models.CharField(max_length=512)

	def __str__(self):
		return self.name

class IllnessAppointment(models.Model):
	date_start = models.DateField(auto_now_add=True)
	date_end = models.DateField(blank=True, null=True)
	illness = models.ForeignKey(IllnessModel, on_delete=models.CASCADE)
	appointment = models.ForeignKey(AppointmentModel, on_delete=models.CASCADE)
	status = models.ForeignKey(StatusModel, on_delete=models.CASCADE)

class VisitModel(models.Model):
	appointment = models.ForeignKey(AppointmentModel, on_delete=models.CASCADE)
	date = models.DateField(auto_now_add=True)
	note = models.CharField(max_length=2056, blank=True)

