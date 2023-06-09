from django.db import models




class Career(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    qualification = models.CharField(max_length=30)
    oppotunities = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    cv = models.FileField()

    def __str__(self):
        return self.name
