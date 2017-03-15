# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_interface_add'),
    ]

    operations = [
        migrations.DeleteModel(
            name='interface_add',
        ),
    ]
