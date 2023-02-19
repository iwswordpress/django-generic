from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("authuser/", include("authuser.urls")),
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("runs/", include("runs.urls", namespace="runs")),
    path("projects/", include("projects.urls", namespace="projects")),
    path('classroom/',include('classroom.urls', namespace="classroom")),
    path('forms/',include('forms.urls', namespace="forms")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    