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
                # run.notebook_file = uploaded_filename
                run.run_id = request.POST.get("run_id")
                run.run_name = request.POST.get("run_name")

                # TODO:Read in file and check if run_id is duplicate
            run.save()

            run_data = {}
            with open(csv_filename, "r") as f:
                csv_reader = csv.reader(f)
                # next(csv_reader) - seems to skip a row after header.
                next(csv_reader)
                for row in csv_reader:
                    # run_id,run_date,project_id,data_scientist_id,mlr_dataset,feature_set,split,split,setup,best,holdout_acc,metrics_dict,accuracy,roc_auc,recall,precision,f1,kappa,mcc
                    print("------------")
                    run_data["run_id"] = row[0]
                    run_data["run_date"] = row[1]
                    run_data["project_id"] = row[2]
                    run_data["data_scientist_id"] = row[3]
                    run_data["mlr_dataset"] = row[4]
                    run_data["feature_set"] = row[5]
                    run_data["split"] = row[6]
                    run_data["setup"] = row[7]
                    run_data["best"] = row[8]
                    run_data["holdout_acc"] = row[9]
                    run_data["metrics_dict"] = row[10]
                    run_data["accuracy"] = row[11]
                    run_data["roc_auc"] = row[12]
                    run_data["recall"] = row[13]
                    run_data["precision"] = row[14]
                    run_data["f1"] = row[15]
                    run_data["kappa"] = row[16]
                    run_data["mcc"] = row[17]
                    print("DATASET is", row[18])
                    print("obj", run_data)

                    updated_run = Run.objects.get(
                        run_id="c5ca764b-27a0-49d1-9482-59aacb9b7903"
                    )
                    print("+++++++++++++++++")
                    print("UPDATED")
                    print(updated_run)
                    runs = Run.objects.all()
                    print(runs)

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
