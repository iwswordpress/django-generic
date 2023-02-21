from django.urls import path
from htmx import views

app_name = "htmx"

urlpatterns = [
    path("", views.check_email_form, name="check-email"),
    path("films/", views.FilmList.as_view(), name="film-list"),
]

htmx_urlpatterns = [
    path("add-film/", views.add_film, name="add-film"),
]

urlpatterns += htmx_urlpatterns
