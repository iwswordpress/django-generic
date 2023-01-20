from django.contrib import admin

# Register your models here.
from .models import Run, TestData

admin.site.register(Run)
admin.site.register(TestData)
