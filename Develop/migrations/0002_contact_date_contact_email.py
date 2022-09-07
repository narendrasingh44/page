# Generated by Django 4.0.6 on 2022-08-13 09:34

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Develop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(default=datetime.datetime(2022, 8, 13, 9, 34, 3, 29123, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]