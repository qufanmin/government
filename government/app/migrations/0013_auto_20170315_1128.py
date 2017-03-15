# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_add'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='add',
            new_name='Interface_add',
        ),
    ]
