from django.urls import path
from . import views

app_name = "forms"

urlpatterns = [
    path("form01/", views.form01_example, name="form01"),
    path("form02/", views.form02_example, name="form02"),
    path("register/", views.registerForm, name="register-form"),
]
