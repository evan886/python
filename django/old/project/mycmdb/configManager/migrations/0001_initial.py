# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='config',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('config_name', models.CharField(max_length=50, verbose_name='\u914d\u7f6e\u540d\u79f0')),
                ('config_type', models.IntegerField(verbose_name='\u6240\u5c5e\u914d\u7f6e\u7c7b\u578b', choices=[(1, '\u7cfb\u7edf\u914d\u7f6e'), (2, '\u5e94\u7528\u914d\u7f6e'), (3, '\u4e2a\u6027\u7cfb\u7edf\u914d\u7f6e'), (4, '\u4e2a\u6027\u5e94\u7528\u914d\u7f6e')])),
                ('config_dir', models.CharField(max_length=255, verbose_name='\u914d\u7f6e\u8def\u5f84')),
                ('availabity', models.BigIntegerField(default=1, verbose_name='\u662f\u5426\u53ef\u7528')),
            ],
            options={
                'db_table': 'config',
            },
        ),
        migrations.AlterUniqueTogether(
            name='config',
            unique_together=set([('config_name', 'availabity')]),
        ),
    ]
