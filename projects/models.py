from django.db import models
import uuid
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
# Create your models here.


class Status(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    status = models.CharField(max_length=20)
    status_order = models.PositiveSmallIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Status'

    def __str__(self):
        return self.status


class Team(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    team_name = models.CharField(max_length=200)

    def __str__(self):
        return self.team_name


class Project(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    project_code = models.CharField(max_length=40, validators=[
        MinLengthValidator(6)], default="MISSING")
    team = models.ForeignKey(
        Team, null=True, blank=False,  on_delete=models.PROTECT, related_name='projects')
    title = models.CharField(max_length=200, validators=[
        MinLengthValidator(3)])
    description = models.TextField(null=True, validators=[
        MinLengthValidator(3)])
    featured_image = models.ImageField(
        null=True, blank=True, default="default.jpg", upload_to='images/projects/')
    status = models.ForeignKey(
        Status, null=True, blank=False,  on_delete=models.PROTECT, related_name='projects')

    def __str__(self):
        return self.title
