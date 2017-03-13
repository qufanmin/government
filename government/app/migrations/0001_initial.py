# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deviceId', models.CharField(max_length=255, null=True)),
                ('deviceModel', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LeakCanaryInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deviceId', models.CharField(max_length=255, null=True)),
                ('deviceModel', models.CharField(max_length=255, null=True)),
                ('version', models.CharField(max_length=20, null=True)),
                ('package', models.CharField(max_length=20, null=True)),
                ('className', models.CharField(max_length=20, null=True)),
                ('leakObj', models.CharField(max_length=20, null=True)),
                ('allText', models.TextField(null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('state', models.IntegerField(null=True)),
                ('operation', models.TextField(null=True)),
            ],
        ),
    ]
