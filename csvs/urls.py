from django.urls import path
from . import views
from . import views_csv

app_name = "csvs"

urlpatterns = [
    path("", views.runs, name="runs"),
    path("upload-csv/", views_csv.uploadCSV, name="upload-csv"),
    path("upload-file-form/", views_csv.uploadCSVFile, name="upload-file-form"),
    path("run/<str:pk>/", views.run, name="run"),
]
