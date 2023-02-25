# Generated by Django 4.1.7 on 2023-02-25 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('csvs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='run',
            name='feature_set',
        ),
        migrations.RemoveField(
            model_name='run',
            name='run_date',
        ),
        migrations.RemoveField(
            model_name='run',
            name='run_name',
        ),
        migrations.RemoveField(
            model_name='run',
            name='setup',
        ),
        migrations.RemoveField(
            model_name='run',
            name='split',
        ),
        migrations.RemoveField(
            model_name='run',
            name='tuned',
        ),
        migrations.RemoveField(
            model_name='run',
            name='uploaded_filename',
        ),
        migrations.AddField(
            model_name='run',
            name='uploaded_file_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='csvs.uploadedfile'),
        ),
    ]