# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configManager', '0001_initial'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='asset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server_type', models.CharField(max_length=30, verbose_name='\u8bbe\u5907\u7c7b\u578b', choices=[('\u4e91\u670d\u52a1\u5668', '\u4e91\u670d\u52a1\u5668'), ('\u4e91\u6570\u636e\u5e93', '\u4e91\u6570\u636e\u5e93'), ('\u4e91\u7f13\u5b58Redis', '\u4e91\u7f13\u5b58Redis')])),
                ('ip', models.CharField(max_length=32, verbose_name='\u7ba1\u7406IP')),
                ('other_ip', models.CharField(max_length=255, null=True, verbose_name='\u5176\u4ed6IP', blank=True)),
                ('port', models.IntegerField(default=22, verbose_name='\u7aef\u53e3\u53f7')),
                ('is_monitoring', models.BooleanField(default=True, verbose_name='\u662f\u5426\u76d1\u63a7')),
                ('is_backup', models.BooleanField(default=True, verbose_name='\u662f\u5426\u5907\u4efd')),
                ('editor', models.TextField(null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('availabity', models.BigIntegerField(default=1, verbose_name='\u662f\u5426\u53ef\u7528')),
                ('app_name', models.ManyToManyField(to='project.app', verbose_name='\u5173\u8054\u5e94\u7528', blank=True)),
                ('config', models.ManyToManyField(to='configManager.config', verbose_name='\u7cfb\u7edf\u914d\u7f6e', blank=True)),
            ],
            options={
                'db_table': 'asset',
            },
        ),
        migrations.CreateModel(
            name='dataCenter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_number', models.CharField(max_length=32, verbose_name='\u4e3b\u8d26\u53f7')),
                ('name', models.CharField(max_length=100, verbose_name='\u540d\u79f0')),
                ('area', models.CharField(max_length=100, verbose_name='\u533a\u57df')),
                ('editor', models.TextField(null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('availabity', models.BigIntegerField(default=1, verbose_name='\u662f\u5426\u53ef\u7528')),
            ],
            options={
                'db_table': 'dataCenter',
            },
        ),
        migrations.AlterUniqueTogether(
            name='datacenter',
            unique_together=set([('name', 'area', 'availabity')]),
        ),
        migrations.AddField(
            model_name='asset',
            name='group',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u6570\u636e\u4e2d\u5fc3', to='assets.dataCenter'),
        ),
        migrations.AddField(
            model_name='asset',
            name='role_name',
            field=models.ManyToManyField(to='project.app_roles', verbose_name='\u5e94\u7528\u89d2\u8272\u540d\u79f0', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='asset',
            unique_together=set([('ip', 'availabity')]),
        ),
    ]
