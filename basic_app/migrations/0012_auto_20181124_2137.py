# Generated by Django 2.0.2 on 2018-11-24 16:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0011_auto_20181124_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogue',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 24, 21, 37, 58, 794700)),
        ),
    ]
