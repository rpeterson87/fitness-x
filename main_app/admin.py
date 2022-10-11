from django.contrib import admin
from .models import Workouts, Exercises, Profile

# Register your models here.

admin.site.register(Workouts)
admin.site.register(Exercises)
admin.site.register(Profile)