import csv

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

from .forms import RunForm
from .models import Run, TestData


from .read_csv import read_csv_test


def runs(request):
    runs = Run.objects.all()
    context = {"runs": runs}
    return render(request, "runs/runs.html", context)


def createRunCSV(request):
    form = RunForm()
    # select read based on file name - export/test/pycaret
    # ===== POST =====
    if request.method == "POST":
        form = RunForm(request.POST, request.FILES)
        uploaded_file = str(request.FILES.get("notebook_file"))
        print("uploaded_file", uploaded_file)

        if form.is_valid():
            form.save()
            # uploaded_file = request.FILES.get("notebook_file")  # ?remove
            if uploaded_file:
                uploads_location = settings.MEDIA_ROOT
                print("location", uploads_location)
                # Get WINDOWS_OS from settings.py as hosting uses non-windows filepath
                if settings.WINDOWS_OS:
                    csv_filename = (
                        str(uploads_location) + "\\data\\" + str(uploaded_file)
                    )
                else:
                    #  File path for: RAILWAY DEPLOYMENT
                    #  RAILWAY  '/app/uploads/data/tests.csv'
                    uploads_location = "/app/uploads"
                    csv_filename = f"{uploads_location}/data/{uploaded_file}"

                print("csv_filename", csv_filename)

            # carry out type of CSV read - tests.csv or pycaret.csv

            # if 'test' in uploaded_file:
            #  TEST.CSV
            read_csv_test(csv_filename)

            # PYCARET.CSV
            # read_csv_pycaret()

        return redirect("runs:runs")
    # ===== END POST =====

    context = {"form": form}
    return render(request, "runs/run-form.html", context)


def run(request, pk):
    run = Run.objects.get(id=pk)
    context = {"run": run}
    return render(request, "runs/run-detail.html", context)


def updateRun(request, pk):
    form = RunForm()
    run = Run.objects.get(id=pk)
    form = RunForm(instance=run)

    if request.method == "POST":

        form = RunForm(request.POST, instance=run)
        if form.is_valid():
            form.save()
            return redirect("runs:runs")

    context = {"form": form}
    return render(request, "runs/run-form.html", context)


def deleteRunConfirm(request, pk):
    print("pk", pk)
    run = Run.objects.get(id=pk)
    context = {"run": run}
    return render(request, "runs/run-delete-confirm.html", context)


def deleteRun(request, pk):
    run = Run.objects.get(id=pk)
    run.delete()
    return redirect("runs:runs")
