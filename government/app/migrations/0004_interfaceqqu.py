# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_interfaceconfigure_personnelconfigure_projectconfigure'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interfaceqqu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('projectName', models.CharField(max_length=255, null=True)),
                ('interfaceName', models.CharField(max_length=255, null=True)),
                ('requestAdress', models.CharField(max_length=255, null=True)),
                ('requestHeader', models.CharField(max_length=255, null=True)),
                ('requestBody', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
