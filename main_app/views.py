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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        workout = self.request.GET.get("workout")
        if workout != None:
            context["artists"] = Workouts.objects.filter(workout__icontains=workout)
            context["header"] = f"Searching for {workout}"
        else:
            context["workouts"] = Workouts.objects.all()   
            context["header"] = f"Searching for {workout}"
        return context
        
    
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["artists"] = artists 
    #     return context