from email.policy import default
from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User

# Create your models here.


# Need to add model for Workouts 
class Workouts(models.Model):

    workout_name = models.CharField(max_length=100)
    video = EmbedVideoField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.workout_name

    class Meta:
        ordering = ['workout_name']
    

# Need to add model for Users 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/')
    bio = models.TextField(default=1) 
    
    def __str__(self):
        return self.user.username
    


# Need to add model for exercises
class Exercises(models.Model):
    sets = models.PositiveBigIntegerField()
    reps = models.PositiveBigIntegerField()
    weight = models.PositiveIntegerField()
    notes = models.CharField(max_length=500)
    performed = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    workout = models.ForeignKey(Workouts, on_delete=models.CASCADE, related_name="workouts")
    # created_by models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.sets
