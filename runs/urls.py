from django.urls import path
from . import views

app_name = "runs"
urlpatterns = [
    path("", views.runs, name="runs"),
#     path("create-run/", views.createRunCSV, name="create-run-csv"),
#     path("run/<str:pk>/", views.run, name="run"),
#     path("run-update/<str:pk>/", views.updateRun, name="run-update"),
#     path(
#         "run-delete-confirm/<str:pk>/",
#         views.deleteRunConfirm,
#         name="run-delete-confirm",
#     ),
#     path("run-delete/<str:pk>/", views.deleteRun, name="run-delete"),
]
