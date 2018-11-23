# Generated by Django 2.0.2 on 2018-11-23 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0005_issueregister'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issueregister',
            old_name='date_time',
            new_name='issue_time',
        ),
        migrations.AddField(
            model_name='issueregister',
            name='return_time',
            field=models.DateTimeField(default=None),
        ),
    ]
