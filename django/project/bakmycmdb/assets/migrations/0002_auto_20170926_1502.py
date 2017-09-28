# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='intraip',
            field=models.CharField(default=0, max_length=32, verbose_name='\u5185\u7f51IP'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='asset',
            name='server_type',
            field=models.CharField(max_length=30, verbose_name='\u8bbe\u5907\u7c7b\u578b', choices=[('\u4e91\u670d\u52a1\u5668', '\u4e91\u670d\u52a1\u5668'), ('\u4e91\u6570\u636e\u5e93mysql', '\u4e91\u6570\u636e\u5e93mysql'), ('\u4e91\u7f13\u5b58Redis', '\u4e91\u7f13\u5b58Redis')]),
        ),
    ]
