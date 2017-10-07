# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_auto_20170926_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='ip',
            field=models.CharField(max_length=32, verbose_name='\u516c\u7f51IP'),
        ),
    ]
