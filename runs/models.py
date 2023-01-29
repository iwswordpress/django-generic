from django.db import models


class Run(models.Model):

    run_id = models.CharField(max_length=255, unique=True, primary_key=True, editable=False,default='ZZZZ')
    run_date = models.DateField(default='2023-01-01')
    project_id = models.PositiveIntegerField(default=1)
    data_scientist_id = models.PositiveIntegerField(default=1)
    mlr_dataset = models.CharField(max_length=255,default="NA")
    feature_set = models.CharField(max_length=255,default="NA")
    split = models.FloatField(default=0.0)
    tuned = models.BooleanField(default=False)
    setup = models.CharField(max_length=1000,default="NA")
    best = models.CharField(max_length=1000,default="NA")
    holdout_acc = models.FloatField()
    metrics_dict = models.CharField(max_length=1000,default="NA")
    accuracy = models.FloatField(default=0.0)
    roc_auc = models.FloatField(default=0.0)
    recall = models.FloatField(default=0.0)
    precision = models.FloatField(default=0.0)
    f1 = models.FloatField(default=0.0)
    kappa = models.FloatField(default=0.0)
    mcc = models.FloatField(default=0.0)
  
    def __str__(self):
        return self.run_id

