import csv
import sqlite3
import uuid


def read_csv_export(file):
    data = []

    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            row = "".join(row)
            row = row.replace(";", " ")
            # print("row is", row)
            data.append(row)
    print("data--->", data)
    return data


def read_csv_test(filename):
    with open(filename) as csv_file:
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
            print("sql = ", sql)


def read_csv_pycaret(file):
    data = []

    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print("row is", row)
            data.append(row)
            print("======================")
    print("pycaret--->", data)
    return data
