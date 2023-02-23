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

from .csv_fns import read_csv_pycaret


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


def uploadCSV(request):
    form = RunForm()
    duplicate_runs = []

    if request.method == "POST":
        print("post form")
        form = RunForm(request.POST, request.FILES)
        print("request.Post", request.POST)
        uploaded_filename = request.FILES.get("uploaded_filename")
        print("uploaded_filename", uploaded_filename)
        if uploaded_filename:
            run = form.save(commit=False)

            if uploaded_filename:

                uploads_location = settings.MEDIA_ROOT
                print("location", uploads_location)
                csv_filename = os.path.join(
                    str(uploads_location), "data", str(uploaded_filename)
                )

                print("csv_filename", csv_filename)

                run.notebook_file = uploaded_filename
                run.data_scientist_id = 1

                # TODO:Read in file and check if run_id is duplicate
            run.save()
            read_csv_pycaret(csv_filename)
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
