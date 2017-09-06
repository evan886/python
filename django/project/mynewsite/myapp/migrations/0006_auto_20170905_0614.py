# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='author_no',
            new_name='author_nos',
        ),
    ]
