from django.urls import path
from . import views
from .views import profile


 


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('workouts/', views.WorkoutsList.as_view(), name="workouts_list"),
    path('workouts/create', views.WorkoutCreate.as_view(), name="workout_create"),
    path('workouts/<int:pk>/', views.WorkoutsDetail.as_view(), name="workouts_detail"),
    path('workouts/<int:pk>/update', views.WorkoutUpdate.as_view(), name="workout_update"),
    path('workouts/<int:pk>/delete', views.WorkoutDelete.as_view(), name="workout_delete"),
    path('workouts/<int:pk>/exercise/new/', views.ExerciseCreate.as_view(), name="exercise_create"),
    # path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('profile/', profile, name='profile'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('update/<int:workout_pk>/exercise/<int:pk>/', views.ExerciseUpdate.as_view(), name="exercise_update"),
    path('exercise/<int:pk>/', views.ExerciseDelete.as_view(), name="exercise_delete"),
] 

