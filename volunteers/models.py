from django.db import models




class Volunteer(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=25)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    area_of_interest = models.CharField(max_length=30)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
