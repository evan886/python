# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20170905_0614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='author_nos',
            new_name='author_no',
        ),
    ]
