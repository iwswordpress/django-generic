from django.shortcuts import render
from .forms import Form01
from .forms import OrderForm


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
        request, "forms/form02.html", {"method": request.method, "form": form}
    )


def registerForm(request):
    return render(request, "forms/register.html", {"method": request.method})


def form01_example(request):
    if request.method == "POST":
        form = Form01(request.POST)
    else:
        form = Form01()

    if request.method == "POST":
        form = Form01(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print("{}: ({}) {}".format(name, type(value), value))

    return render(
        request, "forms/form01.html", {"method": request.method, "form": form}
    )
