# Generated by Django 4.1.7 on 2023-02-25 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='images/profiles/user-default.png', null=True, upload_to='images/profiles/'),
        ),
    ]
