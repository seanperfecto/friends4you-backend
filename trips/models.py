from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trip (models.Model):
    location = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=40)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.title

class Event (models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    start_time = models.DateTimeField
    end_time = models.DateTimeField
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.title
