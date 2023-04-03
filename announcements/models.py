from django.db import models


class Announcement(models.Model):
    content = models.TextField()