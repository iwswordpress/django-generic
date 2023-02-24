import csv
import pandas as pd
import os

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib.auth.models import User
from .models import Run
from .forms import RunForm

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
        # print("post form")
        form = RunForm(request.POST, request.FILES)
        print("request.Post", request.POST)
        uploaded_filename = request.FILES.get("uploaded_filename")
        # print("uploaded_filename", uploaded_filename)
        if uploaded_filename:
            run = form.save(commit=False)

            if uploaded_filename:

                uploads_location = settings.MEDIA_ROOT
                # print("location", uploads_location)
                csv_filename = os.path.join(
                    str(uploads_location), "data", str(uploaded_filename)
                )

                print("csv_filename", csv_filename)
                # run_id,run_date,project_id,data_scientist_id,mlr_dataset,feature_set,split,tuned,setup,best,holdout_acc,metrics_dict,accuracy,roc_auc,recall,precision,f1,kappa,mcc

                run.run_name = request.POST.get("run_name")

                # TODO:Read in file and check if run_id is duplicate
            run.save()

            with open(csv_filename, "r") as f:
                csv_reader = csv.reader(f)
                # next(csv_reader) - seems to skip a row after header.
                next(csv_reader)
                for row in csv_reader:
                    # run_id,run_date,project_id,data_scientist_id,mlr_dataset,feature_set,split,tuned,setup,best,holdout_acc,metrics_dict,accuracy,roc_auc,recall,precision,f1,kappa,mcc
                    print("------------")

                    if 2 == 2:
                        run.run_id = row[0]
                        run.run_date = row[1]
                        run.project_id = row[2]
                        run.data_scientist_id = row[3]
                        run.mlr_dataset = row[4]
                        run.feature_set = row[5]
                        run.split = row[6]
                        if row[7] == "TRUE":
                            run.tuned = True
                        else:
                            run.tuned = False

                        run.setup = row[8]
                        run.model_used = row[9]
                        run.holdout_acc = row[10]
                        run.metrics_dict = row[11]
                        run.accuracy = row[12]
                        run.roc_auc = row[13]
                        run.recall = row[14]
                        run.precision = row[15]
                        run.f1 = row[16]
                        run.kappa = row[17]
                        run.mcc = row[18]
                        run.save()
                    else:
                        print(f"{run.run_id} exists")
                return redirect("csvs:run", pk=run.run_id)
    print("get form")
    context = {"form": form}
    return render(request, "csvs/run-form.html", context)


def run(request, pk):
    # print("pk", pk)
    run = Run.objects.get(run_id=pk)
    print(run)
    context = {"run": run}

    return render(request, "csvs/run-detail.html", context)
