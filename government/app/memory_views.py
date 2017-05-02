# coding:utf-8
from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
from app.models import LeakCanaryInfo,Interfaceqqu,Interface_add,ProjectConfigure
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
    menu_data=ProjectConfigure.objects.all()
    Interface_data=Interface_add.objects.all().order_by("-id")
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
        page = int(request.GET.get("page",1))
        if page < 1:
            page = 1
    except ValueError:
            page = 1
    paginator = Paginator( Interface_data,15)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
         data = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        data = paginator.page(paginator.num_pages)
    return render(request, 'web/interface_config.html', locals())


def memory_info(request):
    id = int(request.GET.get('id', ''))
    data = LeakCanaryInfo.objects.filter(id=id)
    data_list = serializers.serialize("json", data)
    print data_list
    return render(request, 'web/memory_info.html', {'data': data, 'data_list': json.dumps(data_list)})

