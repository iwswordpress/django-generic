# Generated by Django 4.1.7 on 2023-02-24 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvs', '0002_alter_run_id_alter_run_run_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='id',
            field=models.BigIntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
