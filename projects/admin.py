from django.contrib import admin

# Register your models here.
from .models import Project, Team, Status

admin.site.register(Project)
admin.site.register(Status)

admin.site.register(Team)
