# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 18:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookie', '0006_auto_20170820_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='for_main',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_upload',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 21, 18, 1, 40, 144077)),
        ),
    ]
