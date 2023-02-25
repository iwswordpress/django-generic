from django.contrib import admin

# Register your models here.
from .models import Run, UploadedFile

admin.site.register(Run)
admin.site.register(UploadedFile)
