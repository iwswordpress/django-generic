import os
import pandas as pd
import uuid
from sqlalchemy import create_engine
from django.shortcuts import render
from .models import UploadedFile, Test, PycaretRun
from .pandas import get_path


def pandas_home(request):
    folder = "uploads/data/"
    file = "pycaret_results.csv"
    file_path = os.path.join(folder, file)
    # file_path = get_path(folder, file)

    # Join various path components
    try:
        df = pd.read_csv(file_path)
        print(df)
    except:
        pass
    engine = create_engine("sqlite:///db.sqlite3")

    # specify Project table via_meta.db_table
    try:
        df.to_sql(PycaretRun._meta.db_table, if_exists="append", con=engine, index=True)
    except:
        print("ERROR")
        pass

    context = {"info": file_path, "df": df}
    return render(request, "csvs/pandas.html", context)
