from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from .models import Workouts

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"


# Add class for Workouts
class WorkoutsList(TemplateView):
    template_name = "workouts_list.html"
    
    
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["artists"] = artists 
    #     return context