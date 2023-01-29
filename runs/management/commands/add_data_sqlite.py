import pandas as pd
from django.core.management.base import BaseCommand
from runs.models import Run
from sqlalchemy import create_engine

class Command(BaseCommand):
  help = "A command to add data from an Excel file to the database"

  def handle(self, *args, **options):

    print('--> Management Command')

    excel_file = 'pycaret_results_meeting.xlsx'
    df = pd.read_excel(excel_file)
    print(df)
  
    engine = create_engine('sqlite:///db.sqlite3')

    # specify Project table via_meta.db_table
    df.to_sql(Run._meta.db_table, if_exists='replace', con=engine, index=False)
  
