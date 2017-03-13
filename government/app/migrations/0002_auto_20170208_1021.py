# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leakcanaryinfo',
            name='className',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='leakcanaryinfo',
            name='leakObj',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='leakcanaryinfo',
            name='package',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
