# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 20:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20171008_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchstring',
            name='searched_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 10, 8, 1, 36, 39, 278872)),
        ),
    ]
