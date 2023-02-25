import os
import pandas as pd
from django.shortcuts import render
from .models import UploadedFile


def pandas_home(request):
    folder = "uploads"
    file_path = os.path.join(folder, "data", "pycaret_results.csv")
    # Join various path components
    print(file_path)
    try:
        df = pd.read_csv(file_path)
        print(df)
    except:
        pass
    context = {"info": file_path, "df": df}
    return render(request, "csvs/pandas.html", context)
