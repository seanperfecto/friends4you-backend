from django.db import models
from django.contrib.auth.models import User

class Connection (models.Model):
    users = models.ManyToManyField(User)

    def __str__(self):
        return str(self.pk)
