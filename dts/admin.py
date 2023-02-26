from django.contrib import admin

from .models import Run, UploadedFile

admin.site.register(Run)
admin.site.register(UploadedFile)
