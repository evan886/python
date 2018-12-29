# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10, verbose_name='\u540d\u79f0')),
                ('htmlID', models.CharField(max_length=30)),
                ('fatherID', models.IntegerField(default=0, verbose_name='\u4e0a\u7ea7ID')),
                ('icon', models.CharField(max_length=30, null=True, verbose_name='\u5c0f\u56fe\u6807', blank=True)),
                ('htmlClass', models.CharField(max_length=50, null=True, verbose_name='\u6837\u5f0f', blank=True)),
                ('url', models.CharField(max_length=200, verbose_name='\u94fe\u63a5')),
                ('availabity', models.BigIntegerField(default=1)),
            ],
            options={
                'db_table': 'menu',
            },
        ),
        migrations.AlterUniqueTogether(
            name='menu',
            unique_together=set([('htmlID', 'availabity')]),
        ),
    ]
