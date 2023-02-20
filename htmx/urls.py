from django.urls import path
from htmx import views

app_name = "htmx"

urlpatterns = [
    path("", views.check_email_form, name="check-email"),
]

hmtx_views = [
    path("check-username/", views.check_username, name="check-username"),
]

urlpatterns += hmtx_views
