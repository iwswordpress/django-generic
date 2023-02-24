# Generated by Django 4.1.7 on 2023-02-24 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbv', '0002_post_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]