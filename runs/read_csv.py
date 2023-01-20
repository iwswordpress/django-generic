import csv
from .models import TestData

"""Reading CSV files functions."""


def read_csv_test(csv_filename):
    """
    This reads a tests.csv file with columns:
    RUN_ID	 imestamp FILE MODEL_TYPE RND_NUM_HYPER	SPLIT RND_NUM_SPLIT	DO_SCALING ACC
    """
    # TEST.CSV
    with open(csv_filename) as csv_file:
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

            testdata = TestData()
            #  get dict from read_csv_test(file) and then use the values to
            #  load the model instance.
            testdata.run_id = run_id
            testdata.run_date = run_date
            testdata.filename = filename
            testdata.model_type = model_type
            testdata.rnd_num_hyper = rnd_num_hyper
            testdata.split = split
            testdata.rnd_num_split = rnd_num_split
            testdata.is_scaled = is_scaled
            testdata.accuracy = accuracy

            #  save
            testdata.save()

            f"{run_id} \n {run_date} {filename} \n {model_type} \n {rnd_num_hyper} \n {split } \n {rnd_num_split} \n {is_scaled} \n {accuracy} "
    # END TEST.CSV


def read_csv_export(file):
    """
    This reads an exports0X.csv file no columns but each line being a field of data.
    """
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


def read_csv_pycaret(file):
    """
    This reads a pycaret.csv file with columns:
    to be added...
    """
    data = []

    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print("row is", row)
            data.append(row)
    print("pycaret--->", data)
    return data
