# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 18:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cookie', '0007_auto_20170821_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_upload',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 22, 18, 51, 5, 732729, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='alter_descript',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookie.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_upload',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 22, 18, 51, 5, 731367, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(upload_to='product_img'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
