# coding=utf-8
# Create your models here.
from django.db import models


class LeakCanaryInfo(models.Model):
    deviceId = models.CharField(max_length=255, null=True)
    deviceModel = models.CharField(max_length=255, null=True)
    version = models.CharField(max_length=20, null=True)
    package = models.CharField(max_length=20, null=True)
    className = models.CharField(max_length=20, null=True)
    leakObj = models.CharField(max_length=20, null=True)
    allText = models.TextField(null=True)
    creationDate = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField(null=True)
    operation = models.TextField(null=True)


class DeviceInfo(models.Model):
    deviceId = models.CharField(max_length=255, null=True)
    deviceModel = models.CharField(max_length=255, null=True)
