# coding:utf-8
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, response
from app.project_from import ProjectConfigureForm
from app.models import ProjectConfigure, InterfaceConfigure,Interfaceqqu,Interface_add
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from government.common import bigdata_api
import json
import requests
import urllib2

def project_config(request):
    try:
        curPage = int(request.GET.get('curPage', '1'))
        allPage = int(request.GET.get('allPage', '1'))
        pageType = str(request.GET.get('pageType', ''))
        businessName = request.GET.get('businessName', '').encode('utf8')
    except ValueError:
        curPage = 1
        allPage = 1
        pageType = ''
        businessName = ''
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
    print "**************", id
    if businessName != "":
        data = ProjectConfigure.objects.filter(businessName=businessName).order_by("-id")[start:end]
        allPostCounts = ProjectConfigure.objects.filter(businessName=businessName).order_by("-id").count()
    else:
        data = ProjectConfigure.objects.all().order_by("-id")[start:end]
        allPostCounts = ProjectConfigure.objects.all().order_by("-id").count()
    if curPage == 1 and allPage == 1:
        print allPostCounts
        allPage = allPostCounts / 10
        remainPost = allPostCounts % 10
        if remainPost > 0:
            allPage += 1
    return render(request, 'web/project_config.html', {'data': data, 'curPage': curPage,'allPage':allPage})


@csrf_exempt
def project_add(request):
    error = []
    if request.method == 'POST':
        form = ProjectConfigureForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            business = data['businessName']
            project = data['ProjectName']
            assembly = data['assemblyName']
            data = ProjectConfigure(businessName=business, ProjectName=project, assemblyName=assembly)
            data.save()
            return HttpResponseRedirect('/app/project_config/')
        else:
            return render_to_response("web/project_add.html", locals(), RequestContext(request))
    else:
        form = ProjectConfigureForm()
        return render_to_response('web/project_add.html', {'form': form}, context_instance=RequestContext(request))


@csrf_exempt
def project_update(request,id):
    date = get_object_or_404(ProjectConfigure, pk=int(id))
    if request.method == "POST":
        form = ProjectConfigureForm(request.POST, instance=date)
        if form.is_valid():
            date = form.save()
            return HttpResponseRedirect('/app/project_config/')
    return render_to_response('web/project_update.html', {'form': ProjectConfigureForm(instance=date)})


@csrf_exempt
def project_delete(request,id):
    entry = get_object_or_404(ProjectConfigure, pk=int(id))
    entry.delete()
    return HttpResponseRedirect('/app/project_config/')


def interface_add(request):
    string = u"我在自强学堂学习Django，用它来建网站"
#添加接口方法，如果post提交数据，保存到数据库，返回配置页面
# return HttpResponse(u"调试测试")
    if request.method=='POST':
        business=request.POST['business']
        responsible=request.POST['responsible']
        interfaceName=request.POST['interfaceName']
        description=request.POST['description']
        methods=request.POST['methods']
        IP=request.POST['IP']
        interfaceAdress=request.POST['interfaceAdress']
        interfaceBody=request.POST['interfaceBody']
        interfaceDetails=request.POST['interfaceDetails']
        print business+responsible+interfaceName+description+methods+IP+interfaceAdress+interfaceBody+interfaceDetails
        data=Interface_add(business=business,responsible=responsible,interfaceName=interfaceName,description=description,methods=methods,IP=IP,interfaceAdress=interfaceAdress,interfaceBody=interfaceBody,interfaceDetails=interfaceDetails)
        data.save()
        return HttpResponseRedirect('/app/interface_config/')
    else:
        return render(request, 'web/interface_add.html', {'string': string})
#删除接口
def interface_delete(request,id):
    entry = get_object_or_404(Interface_add, pk=int(id))
    entry.delete()
    return HttpResponseRedirect('/app/interface_config')
#编辑接口
def interface_edit(request,id):
    if request.method=='POST':
        business=request.POST['business']
        responsible=request.POST['responsible']
        interfaceName=request.POST['interfaceName']
        description=request.POST['description']
        methods=request.POST['methods']
        IP=request.POST['IP']
        interfaceAdress=request.POST['interfaceAdress']
        interfaceBody=request.POST['interfaceBody']
        interfaceDetails=request.POST['interfaceDetails']
        Interface_add.objects.filter(id=int(id)).update(business=business,responsible=responsible,interfaceName=interfaceName,description=description,methods=methods,IP=IP,interfaceAdress=interfaceAdress,interfaceBody=interfaceBody,interfaceDetails=interfaceDetails)
        return HttpResponseRedirect('/app/interface_config')
    else:
        id=int(id)
        data=Interface_add.objects.filter(id=id)
        return render(request, 'web/interface_edit.html',{'data':data})
#执行接口，发送请求
def interface_request(request,id):
    if request.method=='POST':
        id=int(request.POST['id'])
        urldata=request.POST['url']
        para1=request.POST['header']
        para2= request.POST['body'].encode('utf-8')
        payload=json.loads(para2)
        print type(payload)
        print payload
        responsedata=requests.post(urldata,data=payload)
        data=Interface_add.objects.filter(id=id)
        print id,data,responsedata
#       return render(request, 'web/interface_exe.html',{"data":json.dumps(responsedata.json())},RequestContext(request))
        return render(request, 'web/interface_request.html',{'data':data,'responsedata':responsedata.text})
    else:
        id=int(id)
        data=Interface_add.objects.filter(id=id)
        return render(request, 'web/interface_request.html',{'data':data})
def consultation(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    # return HttpResponse(u"调试测试")
    data = InterfaceConfigure.objects.filter(businessName=u"咨询业务").order_by("-id")
    return render(request, 'web/Consultation.html', {'data': data})


def quotation(request):
    data = InterfaceConfigure.objects.filter(businessName=u"行情信息").order_by("-id")
    # return HttpResponse(u"调试测试")
    print data
    return render(request, 'web/Consultation.html', {'data': data})


def api_details(request):
    id = int(request.GET.get('id', ''))
    data = InterfaceConfigure.objects.filter(id=id)
    print "&&&&&&", data
    return render(request, 'web/api_details.html', {'data': data})
#添加数据接口的函数
@csrf_exempt
def interface_add_qu(request):
    print "$$$$$"
    if request.method=="POST":
        projectName=request.POST["projectName"]
        interfaceName=request.POST["interfaceName"]
        requestAdress=request.POST["requestAdress"]
        requestHeader=request.POST["requestHeader"]
        requestBody=request.POST["requestBody"]
        description=request.POST["description"]
        data=Interfaceqqu(projectName=projectName,interfaceName=interfaceName,requestAdress=requestAdress,requestHeader= requestHeader,requestBody=requestBody,description=description)
        data.save()
        return HttpResponseRedirect('/app/interface_config_qu')
    else:
        data=Interfaceqqu.objects.all()
        print type(data)
        print data
        return render(request, 'web/interface_add2.html',{"data":data})

def interface_exe(request,id):
    id=int(id)
    data=Interfaceqqu.objects.filter(id=id)
    return render(request, 'web/interface_exe.html',{"data":data})
#处理post请求
def interface_exe_request(request):
    id=request.POST['id']
    urldata=request.POST['url']
    para1=request.POST['header']
    para2= request.POST['body']
    payload=json.loads(para2)
    print payload
    print type(payload)
    responsedata=requests.post(urldata,data=payload)
    id=int(id)
    data=Interfaceqqu.objects.filter(id=id)
    print id
#    return render(request, 'web/interface_exe.html',{"data":json.dumps(responsedata.json())},RequestContext(request))
    return render(request, 'web/interface_exe.html',{"responsedata":responsedata.text,"data":data})
#删除接口
@csrf_exempt
def interface_delete_qu(request,id):
    entry = get_object_or_404(Interfaceqqu, pk=int(id))
    entry.delete()
    return HttpResponseRedirect('/app/interface_config_qu')