from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings


class Film(models.Model):
    name = models.CharField(max_length=128)
    # users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="films")
