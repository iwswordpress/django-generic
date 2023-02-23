# %%
"""Read in test.csv and load into run_test table."""
import csv
import sqlite3
import uuid

uuid_val = str(uuid.uuid4())

try:
    sqliteConnection = sqlite3.connect("../../db.sqlite3")
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
except:
    print("did not connect to sqlite")

csv_file = "../../input_data/tests.csv"
with open(csv_file) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # next(csv_reader) - seems to skip a row after header.

    for row in csv_reader:
        print(row)
        run_id = row["RUN_ID"]
        run_date = row["timestamp"]
        filename = row["FILE"]
        model_type = row["MODEL_TYPE"]
        rnd_num_hyper = row["RND_NUM_HYPER"]
        split = row["SPLIT"]
        rnd_num_split = row["RND_NUM_SPLIT"]
        is_scaled = row["DO_SCALING"].lower().capitalize()
        accuracy = row["ACC"]

        print(
            f"{run_id} \n {run_date} {filename} \n {model_type} \n {rnd_num_hyper} \n {split } \n {rnd_num_split} \n {is_scaled} \n {accuracy} "
        )

        sql = f"INSERT INTO runs_testdata (run_id, filename, model_type,run_num_hyper,split,rnd_num_split,is_scaled,accuracy) VALUES('{run_id}','{filename}','{model_type}','{rnd_num_hyper}','{split}','{rnd_num_split}',{is_scaled},{accuracy})"
        print(sql)
        cursor.execute(sql)
        sqliteConnection.commit()
        print("\n\n>>> Record inserted successfully into runs table ")

        print("\ndo sql insert ---->\n", {run_id})

try:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed.")
except:
    print("error closing connection/")
# %%
