from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import FormView, TemplateView
from django.contrib.auth import get_user_model

from htmx.forms import RegisterForm, OrderForm

# Create your views here.


def createTeam(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("htmx:home")

    context = {"form": form}
    print(form)
    return render(request, "htmx/index.html", context)


def form02_example(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
    else:
        form = OrderForm()

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print("{}: ({}) {}".format(name, type(value), value))

    return render(
        request, "htmx/check-email.html", {"method": request.method, "form": form}
    )


def check_username(request):
    username = request.POST.get("username")
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("This username already exists")
    else:
        return HttpResponse("")
