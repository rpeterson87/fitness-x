import imp
from django.contrib import admin
from .models import Workouts, Exercises

# Register your models here.

admin.site.register(Workouts)
admin.site.register(Exercises)