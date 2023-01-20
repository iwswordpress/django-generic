from django.db import models
import uuid
from django.core.validators import MinLengthValidator

# Create your models here.


class Run(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    run_name = models.CharField(
        max_length=100, default="RUN_NAME", validators=[MinLengthValidator(3)]
    )
    project_id = models.PositiveIntegerField(default=0, verbose_name="analyst")
    analyst_id = models.PositiveIntegerField(default=0, verbose_name="analyst")
    purpose = models.CharField(max_length=300, validators=[MinLengthValidator(3)])
    conclusion = models.TextField(null=True, validators=[MinLengthValidator(3)])
    notebook_name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    notebook_location = models.CharField(
        max_length=400, default="LIBRARY", validators=[MinLengthValidator(3)]
    )
    notebook_file = models.FileField(null=True, blank=True, upload_to="data/")
    results = models.TextField(null=True, validators=[MinLengthValidator(3)])
    comments = models.TextField(null=True, validators=[MinLengthValidator(3)])

    def __str__(self):
        return self.run_name


class TestData(models.Model):
    run_id = models.CharField(max_length=100, null=True, blank=True)
    analyst = 1
    filename = models.CharField(
        max_length=200, default="FILE_NAME", null=True, blank=True
    )
    model_type = models.CharField(max_length=20, default="LOG", null=True, blank=True)
    run_num_hyper = models.PositiveIntegerField(
        null=True, blank=True, default=0, verbose_name="random number hyper"
    )
    split = models.FloatField(null=True, blank=True, default=0.2)
    rnd_num_split = models.PositiveIntegerField(
        null=True, blank=True, default=0, verbose_name="random number split"
    )
    is_scaled = models.BooleanField(null=True, blank=True, default=True)
    accuracy = models.FloatField(null=True, blank=True, default=0.0)

    def __str__(self):
        return str(self.run_id)

    # Pluralise name to TestData not TestDatas
