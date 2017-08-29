# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bigint_f', models.BigIntegerField()),
                ('bool_f', models.BooleanField()),
                ('date_f', models.DateField(auto_now=True)),
                ('char_f', models.CharField(unique=True, max_length=20)),
                ('datetime_f', models.DateTimeField(auto_now_add=True)),
                ('decimal_f', models.DecimalField(max_digits=10, decimal_places=2)),
                ('float_f', models.FloatField(null=True)),
                ('int_f', models.IntegerField(default=2010)),
                ('text_f', models.TextField()),
            ],
        ),
    ]
