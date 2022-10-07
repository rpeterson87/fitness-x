from django.db import models

# Create your models here.


# Need to add model for Workouts 
class Workouts(models.Model):

    workout = models.CharField(max_length=100)
    video = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.workout

    class Meta:
        ordering = ['workout']
    

# Need to add model for Users 


# Need to add model for exercises


# Need to add a model for embedded videos