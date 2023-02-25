from django.db import models

import uuid


class UploadedFile(models.Model):

    id = models.CharField(
        max_length=255,
        unique=True,
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    uploaded_name = models.CharField(max_length=100, null=True, blank=True)
    uploaded_filename = models.FileField(null=True, blank=True, upload_to="data/")
    uploaded_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.upload_filename


class Run(models.Model):

    run_id = models.CharField(
        max_length=255,
        unique=True,
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    uploaded_file = models.ForeignKey(UploadedFile, on_delete=models.PROTECT, null=True)
    project_id = models.PositiveIntegerField(default=1)
    data_scientist_id = models.PositiveIntegerField(default=1)
    mlr_dataset = models.CharField(max_length=255, default="datased-used")
    model_used = models.CharField(max_length=1000, default="model-parameters")
    holdout_acc = models.FloatField(default=0.0)
    metrics_dict = models.CharField(max_length=1000, default="{'example_field':'value}")
    accuracy = models.FloatField(default=0.0)
    roc_auc = models.FloatField(default=0.0)
    recall = models.FloatField(default=0.0)
    precision = models.FloatField(default=0.0)
    f1 = models.FloatField(default=0.0)
    kappa = models.FloatField(default=0.0)
    mcc = models.FloatField(default=0.0)

    def __str__(self):
        return self.run_id


class Test(models.Model):
    id = models.CharField(
        max_length=255,
        unique=True,
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    run_id = models.CharField(max_length=255)
    project_id = models.PositiveIntegerField(default=0)
    accuracy = models.FloatField(default=0.0)


# run_id	run_date	project_id	data_scientist_id	mlr_dataset	model_used	holdout_acc	metrics_dict	accuracy	roc_auc	recall	precision	f1	kappa	mcc	uploaded_file

class PycaretRun(models.Model):

    run_id = models.CharField(
        max_length=255,
        unique=True,
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    uploaded_file = models.CharField(max_length=1000, default="UNKNOWN")
    run_date = models.DateTimeField()
    project_id = models.PositiveIntegerField(default=1)
    data_scientist_id = models.PositiveIntegerField(default=1)
    mlr_dataset = models.CharField(max_length=255, default="datased-used")
    model_used = models.CharField(max_length=1000, default="model-parameters")
    holdout_acc = models.FloatField(default=0.0)
    metrics_dict = models.CharField(max_length=1000, default="{'example_field':'value}")
    accuracy = models.FloatField(default=0.0)
    roc_auc = models.FloatField(default=0.0)
    recall = models.FloatField(default=0.0)
    precision = models.FloatField(default=0.0)
    f1 = models.FloatField(default=0.0)
    kappa = models.FloatField(default=0.0)
    mcc = models.FloatField(default=0.0)

    def __str__(self):
        return self.run_id
