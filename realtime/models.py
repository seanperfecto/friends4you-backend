from django.db import models
from django.contrib.auth.models import User

class Connection (models.Model):
    users = models.ManyToManyField(User)
    category = models.IntegerField(default=1)

    def __str__(self):
        return str(self.pk)
