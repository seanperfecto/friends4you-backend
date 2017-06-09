from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trip (models.Model):
    location = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    title = models.CharField(max_length=40)
    users = models.ManyToManyField(User)
