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

    paginator = Paginator(runs, 10)

    page_obj = paginator.get_page(page_number)
    runs = paginator.page(page_number)
    context = {"runs": runs, "page_obj": page_obj}

    return render(request, "runs/runs.html", context)


def createRunCSV(request):
    form = RunForm()

    if request.method == "POST":
        form = RunForm(request.POST, request.FILES)

        if form.is_valid():
            run = form.save(commit=False)
            uploaded_file = request.FILES.get("notebook_file")
            if uploaded_file:

                uploads_location = settings.MEDIA_ROOT
                print("location", uploads_location)
                csv_filename = str(uploads_location) + "\\data\\" + str(uploaded_file)

                print("csv_filename", csv_filename)

                run.notebook_file = uploaded_file
                run.data_scientist_id = 1

                # Read in file and check if run_id is duplicate
            run.save()

            return redirect("runs:runs")

    context = {"form": form}
    return render(request, "runs/run-form.html", context)


def run(request, pk):
    print("pk", pk)
    run = Run.objects.get(run_id=pk)
    print(run)
    context = {"run": run}

    return render(request, "runs/run-detail.html", context)
