from urllib import request
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
# Models
from .models import Workouts, Exercises


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"


# Add class for Workouts
class WorkoutsList(TemplateView):
    template_name = "workouts_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        workout_name = self.request.GET.get("workout_name")
        if workout_name != None:
            context["workout_name"] = Workouts.objects.filter(workout_name__icontains=workout_name)
            context["header"] = f"Searching for {workout_name}"
        else:
            context["workout_name"] = Workouts.objects.all()   
            context["header"] = f"Searching for {workout_name}"
        return context
    
        
class WorkoutCreate(CreateView):
    model = Workouts
    fields = ['workout_name', 'video']
    template_name = "workout_create.html"
    def get_success_url(self):
        return reverse('workouts_detail', kwargs={'pk': self.object.pk})
    
    
    
    
class WorkoutsDetail(DetailView):
    model = Workouts
    template_name = "workouts_detail.html"
    
    
    
class WorkoutUpdate(UpdateView):
    model = Workouts
    fields = ['workout_name', 'video']
    template_name = "workout_update.html"
    def get_success_url(self):
        return reverse('workouts_detail', kwargs={'pk': self.object.pk})
    
    
class WorkoutDelete(DeleteView):
    model = Workouts
    template_name = "workout_delete_confirmation.html"
    success_url = "/workouts/"


class ExerciseCreate(View):
    
    def post(self, request, pk):
        sets = request.POST.get("sets")
        reps = request.POST.get("reps")
        weight = request.POST.get("weight")
        notes = request.POST.get("notes")
        workout = Workouts.objects.get(pk=pk)
        Exercises.objects.create(
            sets=sets,
            reps=reps,
            weight=weight,
            notes=notes,
            workout=workout
            )
        return redirect('workouts_detail', pk=pk)
        
    
    
    
    