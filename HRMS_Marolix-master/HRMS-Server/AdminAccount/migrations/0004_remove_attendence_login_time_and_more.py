# Generated by Django 4.2.1 on 2023-09-22 04:04

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AdminAccount', '0003_attendence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendence',
            name='login_time',
        ),
        migrations.RemoveField(
            model_name='attendence',
            name='logout_time',
        ),
        migrations.AddField(
            model_name='attendence',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='attendence',
            name='punch_times',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='attendence',
            name='total_punch_time',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
    ]