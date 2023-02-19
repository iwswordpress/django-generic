from django.shortcuts import render
from .forms import Form01


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

    return render(request, "forms/form01.html", {"method": request.method, "form": form})

