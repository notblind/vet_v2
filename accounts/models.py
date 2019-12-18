from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group

# Create your models here.

class User(AbstractUser):
    middle_name = models.CharField(max_length=256, blank=True)
    email = models.EmailField(max_length=256, unique=False, blank=True)
    foto = models.ImageField(null=True, blank=True)
