# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from app.models import LeakCanaryInfo, InterfaceConfigure,Interfaceqqu,Interface_add
from django.core import serializers
import json


def memory_management(request):
    try:
        curPage = int(request.GET.get('curPage', '1'))
        allPage = int(request.GET.get('allPage', '1'))
        pageType = str(request.GET.get('pageType', ''))
        deviceModel = request.GET.get('deviceModel', '').encode('utf8')
    except ValueError:
        curPage = 1
        allPage = 1
        pageType = ''
        deviceModel = ''
    if pageType == 'pageDown':
        curPage += 1
    if pageType == 'pageUP':
        curPage -= 1
    start = (curPage - 1) * 10
    end = start + 10
    print "**************", id
    if deviceModel != "":
        data = LeakCanaryInfo.objects.filter(deviceModel=deviceModel).order_by("-id")[start:end]
        allPostCounts = LeakCanaryInfo.objects.filter(deviceModel=deviceModel).order_by("-id").count()
    else:
        data = LeakCanaryInfo.objects.all().order_by("-id")[start:end]
        allPostCounts = LeakCanaryInfo.objects.all().order_by("-id").count()
    if curPage == 1 and allPage == 1:
        print allPostCounts
        allPage = allPostCounts / 10
        remainPost = allPostCounts % 10
        if remainPost > 0:
            allPage += 1
    print '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&', data
    return render(request, 'web/memory_management.html', {'data': data, 'curPage': curPage})


def interface_config(request):
    try:
        curPage = int(request.GET.get('curPage', '1'))
        allPage = int(request.GET.get('allPage', '1'))
        pageType = str(request.GET.get('pageType', ''))
        deviceModel = request.GET.get('deviceModel', '').encode('utf8')
    except ValueError:
        curPage = 1
        allPage = 1
        pageType = ''
        deviceModel = ''
    if pageType == 'pageDown':
        if curPage<allPage:
            curPage += 1
        else:
            curPage=allPage
    if pageType == 'pageUp':
        if curPage==1:
            curPage=1
        else:
            curPage -= 1
    start = (curPage - 1) * 10
    end = start + 10
    print start,end,curPage,allPage
    if deviceModel != "":
        data = Interface_add.objects.filter(deviceModel=deviceModel).order_by("-id")[start:end]
        allPostCounts = Interface_add.objects.filter(deviceModel=deviceModel).order_by("-id").count()
    else:
        data = Interface_add.objects.all().order_by("-id")[start:end]
        allPostCounts = Interface_add.objects.all().order_by("-id").count()
    if curPage == 1 and allPage == 1:
        print allPostCounts
        allPage = allPostCounts / 10
        remainPost = allPostCounts % 10
        if remainPost > 0:
            allPage += 1
    print '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&', data
    return render(request, 'web/interface_config.html', {'data': data, 'curPage': curPage,'allPage':allPage})


def memory_info(request):
    id = int(request.GET.get('id', ''))
    data = LeakCanaryInfo.objects.filter(id=id)
    data_list = serializers.serialize("json", data)
    print data_list
    return render(request, 'web/memory_info.html', {'data': data, 'data_list': json.dumps(data_list)})

def interface_config_qu(request):
    try:
        curPage = int(request.GET.get('curPage', '1'))
        allPage = int(request.GET.get('allPage', '1'))
        pageType = str(request.GET.get('pageType', ''))
        deviceModel = request.GET.get('deviceModel', '').encode('utf8')
    except ValueError:
        curPage = 1
        allPage = 1
        pageType = ''
        deviceModel = ''
    if pageType == 'pageDown':
        curPage += 1
    if pageType == 'pageUP':
        curPage -= 1
    start = (curPage - 1) * 10
    end = start + 10
    print "**************", id
    if deviceModel != "":
        data = Interfaceqqu.objects.all()
        allPostCounts = Interfaceqqu.objects.all().count()
    else:
        data = Interfaceqqu.objects.all()
        allPostCounts = Interfaceqqu.objects.all().count()
    if curPage == 1 and allPage == 1:
        print allPostCounts
        allPage = allPostCounts / 10
        remainPost = allPostCounts % 10
        if remainPost > 0:
            allPage += 1
    print '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&', data
    return render(request, 'web/interface_config2.html', {'data': data, 'curPage': curPage})