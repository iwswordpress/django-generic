from django.urls import path
from . import views
from . import views_dts
from . import views_pd

app_name = "dts"

urlpatterns = [
    path("", views.runs, name="runs"),
    # path("upload-csv/", views_csv.uploadCSV, name="upload-csv"),
    path("upload-file-form/", views_dts.uploadCSVFile, name="upload-file-form"),
    path("run/<str:pk>/", views.run, name="run"),
    path("pandas/", views_pd.pandas_home, name="pandas"),
]
