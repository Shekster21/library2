# Generated by Django 2.0.2 on 2018-11-24 13:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0007_auto_20181124_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogue',
            name='curr_user',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='catalogue',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 24, 19, 29, 54, 408424)),
        ),
    ]
