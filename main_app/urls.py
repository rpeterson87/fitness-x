from unicodedata import name
from django.urls import path, include
from . import views
 


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('workouts/', views.WorkoutsList.as_view(), name="workouts_list"),
    path('workouts/create/', views.WorkoutCreate.as_view(), name="workout_create"),
]
