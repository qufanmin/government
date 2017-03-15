# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_delete_interface_add'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interface_add',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('business', models.CharField(max_length=255, null=True)),
                ('responsible', models.CharField(max_length=255, null=True)),
                ('interfaceName', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('methods', models.CharField(max_length=255, null=True)),
                ('IP', models.CharField(max_length=255, null=True)),
                ('interfaceAdress', models.CharField(max_length=255, null=True)),
                ('interfaceBody', models.CharField(max_length=1000, null=True)),
                ('interfaceDetails', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
