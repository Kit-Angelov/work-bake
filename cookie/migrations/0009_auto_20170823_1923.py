# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 19:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cookie', '0008_auto_20170822_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='hit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='photo_for_slider',
            field=models.ImageField(blank=True, null=True, upload_to='slider_img'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_upload',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 19, 23, 47, 144941, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_upload',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 19, 23, 47, 142969, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(upload_to='product_img', verbose_name='Фото'),
        ),
    ]