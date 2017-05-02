# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from government.common.db_config import db_conn
from app.models import ProjectConfigure,PersonnelConfigure
from app.forms import PersonnelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
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
    datas=PersonnelConfigure.objects.all().order_by("-id")
    menu_data=ProjectConfigure.objects.all()
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
        page = int(request.GET.get("page",1))
        if page < 1:
            page = 1
    except ValueError:
            page = 1
    paginator = Paginator( datas,15)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
         data = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        data = paginator.page(paginator.num_pages)
    return render(request, 'web/personnel_config.html', locals())
def personnel_add(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    # return HttpResponse(u"调试测试")
    error = []
    if request.method=='POST':
        form = PersonnelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/app/personnel_config/')
        else:
            return render_to_response("web/personnel_add.html", locals(), RequestContext(request))
    menu_data=ProjectConfigure.objects.all()
    form=PersonnelForm()
    return render(request, 'web/personnel_add.html', locals())
@csrf_exempt
def personnel_update(request,id):
    date = get_object_or_404(PersonnelConfigure, pk=int(id))
    menu_data=ProjectConfigure.objects.all()
    print date
    if request.method == "POST":
        form = PersonnelForm(request.POST, instance=date)
        if form.is_valid():
            date = form.save()
            return HttpResponseRedirect('/app/personnel_config/')
    return render_to_response('web/personnel_update.html', {'form': PersonnelForm(instance=date),'menu_bigdata':menu_bigdata,'menu_app':menu_app},context_instance=RequestContext(request))
def personnel_delete(request,id):
     entry = get_object_or_404(PersonnelConfigure, pk=int(id))
     try:
        entry.delete()
     except Exception,e:
        data = PersonnelConfigure.objects.all().order_by("-id")
        error=u'请先删除关联的接口'
        return render_to_response('web/personnel_config.html',locals())
     return HttpResponseRedirect('/app/personnel_config/')
def project_add(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    # return HttpResponse(u"调试测试")
    return render(request, 'web/project_add.html', {'string': string})





