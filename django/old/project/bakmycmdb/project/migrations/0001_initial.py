# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='app',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u5e94\u7528\u540d\u79f0')),
                ('another_name', models.CharField(max_length=30, null=True, verbose_name='\u522b\u540d', blank=True)),
                ('architecture', models.CharField(max_length=255, null=True, verbose_name='\u67b6\u6784\u56fe', blank=True)),
                ('availabity', models.BigIntegerField(default=1, verbose_name='\u662f\u5426\u53ef\u7528')),
            ],
            options={
                'db_table': 'app',
            },
        ),
        migrations.CreateModel(
            name='app_roles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('appid', models.ForeignKey(to='project.app')),
            ],
            options={
                'db_table': 'app_roles',
            },
        ),
        migrations.CreateModel(
            name='appRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u89d2\u8272\u540d\u79f0')),
                ('availabity', models.BigIntegerField(default=1, verbose_name='\u662f\u5426\u53ef\u7528')),
            ],
            options={
                'db_table': 'appRole',
            },
        ),
        migrations.AlterUniqueTogether(
            name='approle',
            unique_together=set([('name', 'availabity')]),
        ),
        migrations.AddField(
            model_name='app_roles',
            name='roleid',
            field=models.ForeignKey(to='project.appRole'),
        ),
        migrations.AddField(
            model_name='app',
            name='roles',
            field=models.ManyToManyField(to='project.appRole', verbose_name='\u89d2\u8272', through='project.app_roles', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='app',
            unique_together=set([('name', 'another_name', 'availabity')]),
        ),
    ]
