import csv
import pandas as pd
import os

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib.auth.models import User
from .models import Run, UploadedFile
from .forms import UploadedFileForm

from .csv_fns import read_csv_pycaret


def uploadCSVFile(request):
    form = UploadedFileForm()
    if request.method == "POST":
        form = UploadedFileForm(request.POST, request.FILES)
        print("request.POST", request.POST)
        uploaded_filename = request.FILES.get("uploaded_filename")
        print("uploaded_filename", uploaded_filename)
        if uploaded_filename:
            uploaded = form.save(commit=False)

            if uploaded_filename:

                uploads_location = settings.MEDIA_ROOT
                print("location", uploads_location)
                csv_filename_path = os.path.join(
                    str(uploads_location), "data", str(uploaded_filename)
                )

                print("csv_filename_path", csv_filename_path)

            uploaded.save()

    context = {"form": form}
    return render(request, "csvs/upload-file-form.html", context)


# def uploadCSV(request):
#     form = RunForm()
#     duplicate_runs = []

#     if request.method == "POST":
#         # print("post form")
#         form = RunForm(request.POST, request.FILES)
#         print("request.Post", request.POST)
#         uploaded_filename = request.FILES.get("uploaded_filename")
#         # print("uploaded_filename", uploaded_filename)
#         if uploaded_filename:
#             run = form.save(commit=False)

#             if uploaded_filename:

#                 uploads_location = settings.MEDIA_ROOT
#                 # print("location", uploads_location)
#                 csv_filename = os.path.join(
#                     str(uploads_location), "data", str(uploaded_filename)
#                 )

#                 print("csv_filename", csv_filename)
#                 # run_id,run_date,project_id,data_scientist_id,mlr_dataset,feature_set,split,tuned,setup,best,holdout_acc,metrics_dict,accuracy,roc_auc,recall,precision,f1,kappa,mcc

#             # run.save()

#     print("get form")
#     context = {"form": form}
#     return render(request, "csvs/run-form.html", context)
