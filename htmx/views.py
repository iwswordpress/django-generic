from django.shortcuts import render
from .models import Film
from django.views.generic.list import ListView
from htmx.forms import CheckEmail, AddFilm

# Create your views here.


def check_email_form(request):
    if request.method == "POST":
        form = CheckEmail(request.POST)
    else:
        form = CheckEmail()

    if request.method == "POST":
        form = CheckEmail(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print("{}: ({}) {}".format(name, type(value), value))

    return render(
        request, "htmx/check-email.html", {"method": request.method, "form": form}
    )


class FilmList(ListView):
    template_name = "htmx/films.html"
    model = Film
    context_object_name = "films"

    # def get_queryset(self):
    #     user = self.request.user
    #     return user.films.all()


def add_film(request):
    if request.method == "POST":
        form = AddFilm(request.POST)

        if form.is_valid():
            film = Film(name=form.cleaned_data["name"])
            film.save()
            for name, value in form.cleaned_data.items():
                print("{}: ({}) {}".format(name, type(value), value))
    else:
        form = AddFilm()

    return render(request, "htmx/films.html", {"method": request.method, "form": form})
