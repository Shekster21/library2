# Generated by Django 2.0.2 on 2018-11-23 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0003_catalogue_curr_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='batch',
            field=models.CharField(default='a', max_length=1),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='register_number',
            field=models.CharField(default='xxxx', max_length=10),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='semester',
            field=models.IntegerField(default=1),
        ),
    ]
