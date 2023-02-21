from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings


class Film(models.Model):
    name = models.CharField(max_length=50)
    user_id = models.SmallIntegerField(default=1)
