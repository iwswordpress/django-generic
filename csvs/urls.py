from django.urls import path
from . import views
from . import views_csv
from . import views_pd

app_name = "csvs"

urlpatterns = [
    path("", views.runs, name="runs"),
    path("upload-file-form/", views_csv.uploadCSVFile, name="upload-file-form"),
    path("run/<str:pk>/", views.run, name="run"),
    path("pandas/", views_pd.pandas_home, name="pandas"),
]
