from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()



class Event(models.Model):
    event_image = models.ImageField(upload_to="event_images", blank=True)
    host = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    registrants = models.ManyToManyField(User, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start = models.DateTimeField()
    end =  models.DateTimeField()


    def __str__(self):
        return self.name
