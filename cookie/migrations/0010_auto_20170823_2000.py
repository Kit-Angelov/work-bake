# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 20:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cookie', '0009_auto_20170823_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_upload',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 20, 0, 35, 971814, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_upload',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 20, 0, 35, 968761, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(upload_to='cookie/media', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo_for_slider',
            field=models.ImageField(blank=True, null=True, upload_to='cookie/media'),
        ),
    ]
