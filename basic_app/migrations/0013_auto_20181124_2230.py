# Generated by Django 2.0.2 on 2018-11-24 17:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0012_auto_20181124_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='issueregister',
            name='returned',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='catalogue',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 24, 22, 30, 45, 417887)),
        ),
    ]
