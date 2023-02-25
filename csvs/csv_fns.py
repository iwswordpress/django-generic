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
    run = {"id": ""}

    with open(file, "r") as f:
        csv_reader = csv.reader(f)
        # next(csv_reader) - seems to skip a row after header.
        next(csv_reader)
        for row in csv_reader:
            # run_id,run_date,project_id,data_scientist_id,mlr_dataset,feature_set,split,tuned,setup,best,holdout_acc,metrics_dict,accuracy,roc_auc,recall,precision,f1,kappa,mcc

            print("======================")
            run_id = row[0]
            print("FN run_id:", run_id)

    return run_id

    #   with open(csv_filename, "r") as f:
    #             csv_reader = csv.reader(f)
    #             # next(csv_reader) - seems to skip a row after header.
    #             next(csv_reader)
    #             for row in csv_reader:
    #                 # run_id,run_date,project_id,data_scientist_id,mlr_dataset,feature_set,split,tuned,setup,best,holdout_acc,metrics_dict,accuracy,roc_auc,recall,precision,f1,kappa,mcc
    #                 print("------------")

    #                 if 2 == 2:
    #                     run.run_id = row[0]
    #                     run.run_date = row[1]
    #                     run.project_id = row[2]
    #                     run.data_scientist_id = row[3]
    #                     run.mlr_dataset = row[4]
    #                     run.feature_set = row[5]
    #                     run.split = row[6]
    #                     if row[7] == "TRUE":
    #                         run.tuned = True
    #                     else:
    #                         run.tuned = False

    #                     run.setup = row[8]
    #                     run.model_used = row[9]
    #                     run.holdout_acc = row[10]
    #                     run.metrics_dict = row[11]
    #                     run.accuracy = row[12]
    #                     run.roc_auc = row[13]
    #                     run.recall = row[14]
    #                     run.precision = row[15]
    #                     run.f1 = row[16]
    #                     run.kappa = row[17]
    #                     run.mcc = row[18]
    #                     run.save()
    #                 else:
    #                     print(f"{run.run_id} exists")
    #             return redirect("csvs:run", pk=run.run_id)
