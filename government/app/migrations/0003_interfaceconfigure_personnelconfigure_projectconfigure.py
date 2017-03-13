# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170208_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterfaceConfigure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('businessName', models.CharField(max_length=255, null=True)),
                ('businessDescribe', models.CharField(max_length=255, null=True)),
                ('InterfaceName', models.CharField(max_length=255, null=True)),
                ('requestMode', models.CharField(max_length=255, null=True)),
                ('ipAddress', models.CharField(max_length=255, null=True)),
                ('InterfaceURL', models.CharField(max_length=255, null=True)),
                ('InterfaceIP', models.CharField(max_length=255, null=True)),
                ('AdministrationName', models.CharField(max_length=255, null=True)),
                ('describe', models.TextField(null=True)),
                ('info', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonnelConfigure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('businessName', models.CharField(max_length=255, null=True)),
                ('businessModular', models.CharField(max_length=255, null=True)),
                ('ModularAdministration', models.CharField(max_length=255, null=True)),
                ('describe', models.TextField(null=True)),
                ('info', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectConfigure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('businessName', models.CharField(max_length=255, null=True)),
                ('ProjectName', models.CharField(max_length=255, null=True)),
                ('assemblyName', models.CharField(max_length=255, null=True)),
                ('ProjectAdministration', models.CharField(max_length=255, null=True)),
                ('SoftwareAdministration', models.CharField(max_length=255, null=True)),
                ('TestAdministration', models.CharField(max_length=255, null=True)),
                ('describe', models.TextField(null=True)),
                ('info', models.TextField(null=True)),
            ],
        ),
    ]
