from django.urls import path
from . import views

app_name = "csvs"

urlpatterns = [
    path("", views.runs, name="runs"),
    path("create-run/", views.createRunCSV, name="create-run-csv"),
    path("run/<str:pk>/", views.run, name="run"),
]
