# coding=utf-8
# Create your models here.
from django.db import models


class LeakCanaryInfo(models.Model):
    deviceId = models.CharField(max_length=255, null=True)
    deviceModel = models.CharField(max_length=255, null=True)
    version = models.CharField(max_length=20, null=True)
    package = models.CharField(max_length=255, null=True)
    className = models.CharField(max_length=255, null=True)
    leakObj = models.CharField(max_length=255, null=True)
    allText = models.TextField(null=True)
    creationDate = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField(null=True)
    operation = models.TextField(null=True)


class DeviceInfo(models.Model):
    deviceId = models.CharField(max_length=255, null=True)
    deviceModel = models.CharField(max_length=255, null=True)


# 接口信息配置
class InterfaceConfigure(models.Model):
    businessName = models.CharField(max_length=255, null=True)
    businessDescribe = models.CharField(max_length=255, null=True)
    InterfaceName = models.CharField(max_length=255, null=True)
    requestMode = models.CharField(max_length=255, null=True)
    ipAddress = models.CharField(max_length=255, null=True)
    InterfaceURL = models.CharField(max_length=255, null=True)
    InterfaceIP = models.CharField(max_length=255, null=True)
    AdministrationName = models.CharField(max_length=255, null=True)
    describe = models.TextField(null=True)
    info = models.TextField(null=True)


# 项目信息信息配置
class ProjectConfigure(models.Model):
    businessName = models.CharField(max_length=255, null=True)
    ProjectName = models.CharField(max_length=255, null=True)
    assemblyName = models.CharField(max_length=255, null=True)
    ProjectAdministration = models.CharField(max_length=255, null=True)
    SoftwareAdministration = models.CharField(max_length=255, null=True)
    TestAdministration = models.CharField(max_length=255, null=True)
    describe = models.TextField(null=True)
    info = models.TextField(null=True)


# 项目人员配置
class PersonnelConfigure(models.Model):
    businessName = models.CharField(max_length=255, null=True)
    businessModular = models.CharField(max_length=255, null=True)
    ModularAdministration = models.CharField(max_length=255, null=True)
    describe = models.TextField(null=True)
    info = models.TextField(null=True)
#屈凡民接口添加保存到数据库
class Interfaceqqu(models.Model):
	projectName=models.CharField(max_length=255, null=True)
	interfaceName=models.CharField(max_length=255, null=True)
	requestAdress=models.CharField(max_length=255, null=True)
	requestHeader=models.CharField(max_length=255, null=True)
	requestBody=models.CharField(max_length=255, null=True)
	description=models.CharField(max_length=255, null=True)
def __unicode__(self):
	return self.interfaceName