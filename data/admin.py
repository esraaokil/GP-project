from django.contrib import admin
from .models import Profile,Doctor,Patient,Review,ChestDetails,Chronic_diseases,Patient_chronic_diseases
# Register your models here.

admin.site.register(Profile)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Review)
admin.site.register(ChestDetails)
admin.site.register(Chronic_diseases)
admin.site.register(Patient_chronic_diseases)