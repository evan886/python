# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-30 14:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20170429_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 30, 14, 0, 37, 15553, tzinfo=utc)),
        ),
    ]