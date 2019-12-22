from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(IllnessModel)
admin.site.register(AppointmentModel)
admin.site.register(StatusModel)
admin.site.register(IllnessAppointment)
admin.site.register(VisitModel)