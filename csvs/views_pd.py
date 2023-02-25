import os
import pandas as pd
from django.shortcuts import render
from .models import UploadedFile
from .pandas import get_path


def pandas_home(request):
    folder = "uploads/data/"
    file = "pycaret_results.csv"
    file_path = os.path.join(folder, file)
    # file_path = get_path(folder, file)

    # Join various path components
    try:
        df = pd.read_csv(file_path)
        # print(df)
    except:
        pass
    context = {"info": file_path, "df": df}
    return render(request, "csvs/pandas.html", context)
