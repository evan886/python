# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='domainName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\x9f\x9f\xe5\x90\x8d')),
                ('nameDistributor', models.CharField(max_length=50, verbose_name=b'\xe5\x9f\x9f\xe5\x90\x8d\xe4\xbe\x9b\xe5\xba\x94\xe5\x95\x86')),
                ('exptresDate', models.CharField(max_length=20, verbose_name=b'\xe5\x88\xb0\xe6\x9c\x9f\xe6\x97\xb6\xe9\x97\xb4')),
                ('user', models.CharField(max_length=50, verbose_name=b'\xe6\xb3\xa8\xe5\x86\x8c\xe7\x94\xa8\xe6\x88\xb7')),
                ('email', models.CharField(max_length=50, verbose_name=b'\xe6\xb3\xa8\xe5\x86\x8c\xe9\x82\xae\xe7\xae\xb1')),
                ('organization', models.CharField(max_length=50, verbose_name=b'\xe6\xb3\xa8\xe5\x86\x8c\xe5\x85\xac\xe5\x8f\xb8')),
                ('availabity', models.BigIntegerField(default=1, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x8f\xaf\xe7\x94\xa8')),
            ],
            options={
                'db_table': 'domainName',
            },
        ),
        migrations.AlterUniqueTogether(
            name='domainname',
            unique_together=set([('name', 'availabity')]),
        ),
    ]
