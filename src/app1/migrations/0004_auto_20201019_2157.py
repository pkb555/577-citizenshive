# Generated by Django 3.1.2 on 2020-10-20 04:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20201019_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='senior',
            name='availability',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='senior',
            name='bio',
            field=models.TextField(blank=True, max_length=1024),
        ),
        migrations.AddField(
            model_name='senior',
            name='city',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='senior',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='senior',
            name='state',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='senior',
            name='zip_code',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='comments',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2020, 10, 19, 21, 57, 41, 476925)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2020, 10, 19, 21, 57, 41, 476925)),
        ),
        migrations.AlterField(
            model_name='senior',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
