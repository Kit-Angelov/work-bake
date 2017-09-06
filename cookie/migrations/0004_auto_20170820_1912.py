# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 19:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookie', '0003_auto_20170820_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='alter_descript',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='product_img'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_upload',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 20, 19, 12, 45, 940946)),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_upload',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
