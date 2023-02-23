from django.urls import path
from . import views

app_name = "csvs"

urlpatterns = [
    path("", views.runs, name="runs"),
    path("upload-csv/", views.uploadCSV, name="upload-csv"),
    path("run/<str:pk>/", views.run, name="run"),
]
