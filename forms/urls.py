from django.urls import path
from . import views

app_name = 'forms'

urlpatterns = [
    path('', views.form01_example, name="home"),
   
]
