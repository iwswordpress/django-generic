import os
import pandas as pd
import uuid
from sqlalchemy import create_engine
from django.shortcuts import render
from .models import UploadedFile, Test, PycaretRun
from .pandas import get_path


def pandas_home(request):
    folder = "uploads/data/"
    file = "pycaret_results_meeting.xlsx"
    file = "pycaret_results_meeting.csv"
    file_path = os.path.join(folder, file)
    # file_path = get_path(folder, file)
    # df = pd.read_excel(file_path)

    df = pd.read_csv(file_path)
    print(df)

    engine = create_engine("sqlite:///db.sqlite3")

    # specify Project table via_meta.db_table
    df.to_sql(PycaretRun._meta.db_table, if_exists="append", con=engine, index=False)
    df.to_sql(name="dts_new", con=engine)

    context = {"info": file_path, "df": df}
    return render(request, "csvs/pandas.html", context)
