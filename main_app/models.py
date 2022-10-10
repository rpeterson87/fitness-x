from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.


# Need to add model for Workouts 
class Workouts(models.Model):

    workout_name = models.CharField(max_length=100)
    video = EmbedVideoField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.workout_name

    class Meta:
        ordering = ['workout_name']
    

# Need to add model for Users 


# Need to add model for exercises


# Need to add a model for embedded videos