# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse


def memory_management(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    # return HttpResponse(u"调试测试")
    return render(request, 'web/memory_management.html', {'string': string})


def memory_info(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    # return HttpResponse(u"调试测试")
    return render(request, 'web/memory_info.html', {'string': string})
