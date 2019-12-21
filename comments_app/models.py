from django.db import models
from personal.models import ClientModel
# Create your models here.

class CommentsModel(models.Model):
	client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
	message = models.CharField(max_length=3000)
	timedate = models.DateTimeField(auto_now_add=True)
