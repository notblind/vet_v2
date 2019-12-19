from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(ClientModel)
admin.site.register(DistrictModel)
admin.site.register(StaffModel)

admin.site.register(AnimalModel)
admin.site.register(BreedModel)
admin.site.register(AnimaClientModel)