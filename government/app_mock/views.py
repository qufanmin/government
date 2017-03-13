# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from government.common.db_config import db_conn


def login(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    # return HttpResponse(u"调试测试")
    return render(request, 'web/login.html', {'string': string})


def api_data(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    # return HttpResponse(u"调试测试")
    return render(request, 'web/api_data.html', {'string': string})


def test(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    # return HttpResponse(u"调试测试")
    return render(request, 'web/test.html', {'string': string})


def data(request):
    db_conn()
    string = u"我在自强学堂学习Django，用它来建网站"
    # return HttpResponse(u"调试测试")
    return render(request, 'web/data.html', {'string': string})


def interface_config(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    # return HttpResponse(u"调试测试")
    return render(request, 'web/Interface_config.html', {'string': string})


def personnel_config(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    # return HttpResponse(u"调试测试")
    return render(request, 'web/personnel_config.html', {'string': string})


def project_config(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    # return HttpResponse(u"调试测试")
    return render(request, 'web/project_config.html', {'string': string})


