import csv
import pandas as pd
import os

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib.auth.models import User
from .models import Run
from .forms import RunForm
from .models import Run


def runs(request):
    runs = Run.objects.all()
    page_number = request.GET.get("page")
    if not page_number:
        page_number = 1

    paginator = Paginator(runs, 5)

    page_obj = paginator.get_page(page_number)
    runs = paginator.page(page_number)
    context = {"runs": runs, "page_obj": page_obj}

    return render(request, "csvs/runs.html", context)


def createRunCSV(request):
    form = RunForm()
    duplicate_runs = []

    if request.method == "POST":
        print("post form")
        form = RunForm(request.POST, request.FILES)

        if form.is_valid():
            run = form.save(commit=False)

            uploaded_file = request.FILES.get("notebook_file")
            print("uploaded file", uploaded_file)

            run.save()
            return redirect("csvs:run", pk=run.run_id)
    print("get form")
    context = {"form": form}
    return render(request, "csvs/run-form.html", context)


def run(request, pk):
    print("pk", pk)
    run = Run.objects.get(run_id=pk)
    print(run)
    context = {"run": run}

    return render(request, "csvs/run-detail.html", context)
