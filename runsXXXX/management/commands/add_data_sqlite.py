import pandas as pd
from django.core.management.base import BaseCommand
from runs.models import Run
from sqlalchemy import create_engine


class Command(BaseCommand):
    help = "A command to add data from an Excel file to the database"

    def handle(self, *args, **options):

        print("--> Management Command")

        excel_file = "./uploads/data/pycaret.xlsx"
        csv_file = "./uploads/data/pycaret_csv.csv"
        # df = pd.read_excel(excel_file)
        df = pd.read_csv(csv_file)
        print(df)

        engine = create_engine("sqlite:///db.sqlite3")

        # specify Project table via_meta.db_table
        df.to_sql(Run._meta.db_table, if_exists="append", con=engine, index=False)
