# coding:utf-8
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from app.project_from import ProjectConfigureForm
from app.models import ProjectConfigure, InterfaceConfigure,Interfaceqqu,Interface_add,PersonnelConfigure
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import copy
import time
import os
from app.forms import InterfaceForm
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
def project_config(request):
    datas = ProjectConfigure.objects.all().order_by("-id")
    allPostCounts = ProjectConfigure.objects.all().order_by("-id").count()
    menu_app=ProjectConfigure.objects.filter(businessName=u'APP组').values('ProjectName').distinct()
    menu_bigdata=ProjectConfigure.objects.filter(businessName=u'大数据服务组').values('ProjectName').distinct()
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
    return render(request, 'web/project_config.html', locals())


@csrf_exempt
def project_add(request):
    error = []
    menu_app=ProjectConfigure.objects.filter(businessName=u'APP组').values('ProjectName').distinct()
    menu_bigdata=ProjectConfigure.objects.filter(businessName=u'大数据服务组').values('ProjectName').distinct()
    if request.method == 'POST':
        form = ProjectConfigureForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/app/project_config/')
        else:
            return render_to_response("web/project_add.html", locals(), RequestContext(request))
    else:
        datas=ProjectConfigure.objects.all()
        data=[]
        for item in datas:
            select=(item.ProjectName,item.ProjectName)
            data.append(select)
        form = ProjectConfigureForm()
        return render_to_response('web/project_add.html', {'form': form,'menu_bigdata':menu_bigdata,'menu_app':menu_app}, context_instance=RequestContext(request))


@csrf_exempt
def project_update(request,id):
    date = get_object_or_404(ProjectConfigure, pk=int(id))
    menu_app=ProjectConfigure.objects.filter(businessName=u'APP组').values('ProjectName').distinct()
    menu_bigdata=ProjectConfigure.objects.filter(businessName=u'大数据服务组').values('ProjectName').distinct()
    print date
    if request.method == "POST":
        form = ProjectConfigureForm(request.POST, instance=date)
        if form.is_valid():
            date = form.save()
            return HttpResponseRedirect('/app/project_config/')
    return render_to_response('web/project_update.html', {'form': ProjectConfigureForm(instance=date),'menu_bigdata':menu_bigdata,'menu_app':menu_app})


@csrf_exempt
def project_delete(request,id):
    entry = get_object_or_404(ProjectConfigure, pk=int(id))
    entry.delete()
    return HttpResponseRedirect('/app/project_config/')


def interface_add(request):
    errors=[]
#添加接口方法，如果post提交数据，保存到数据库，返回配置页面
# return HttpResponse(u"调试测试")
    if request.method=='POST':
        form=InterfaceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/app/interface_config/')
        else:
            return render_to_response( 'web/interface_add.html',locals(),RequestContext(request))
    else:
        menu_app=ProjectConfigure.objects.filter(businessName=u'APP组').values('ProjectName').distinct()
        menu_bigdata=ProjectConfigure.objects.filter(businessName=u'大数据服务组').values('ProjectName').distinct()
        form=InterfaceForm()
        return render(request, 'web/interface_add.html',locals(), RequestContext(request))
#删除接口
def interface_delete(request,id):
    entry = get_object_or_404(Interface_add, pk=int(id))
    entry.delete()
    return HttpResponseRedirect('/app/interface_config')
#编辑接口
@csrf_exempt
def interface_edit(request,id):
    menu_app=ProjectConfigure.objects.filter(businessName=u'APP组').values('ProjectName').distinct()
    menu_bigdata=ProjectConfigure.objects.filter(businessName=u'大数据服务组').values('ProjectName').distinct()
    #date = get_object_or_404(Interface_add, pk=int(id))
    data=Interface_add.objects.filter(id=int(id))
    for item in data:
        business=item.business
        responsible=item.responsible
    date = Interface_add.objects.get(pk=int(id))
    business_id=ProjectConfigure.objects.filter(ProjectName=business)[0].id
    responsible_id=PersonnelConfigure.objects.filter(ModularAdministration=responsible)[0].id
    print business_id,responsible_id
    if request.method == "POST":
        form = InterfaceForm(request.POST, instance=date)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect('/app/interface_config')
    return render_to_response('web/interface_edit.html', {'form': InterfaceForm(initial={'business': business_id,'responsible':responsible_id},instance=date),'menu_bigdata':menu_bigdata,'menu_app':menu_app},context_instance=RequestContext(request))
#复制接口
def interface_copy(request,id):
    data=copy.deepcopy(Interface_add.objects.get(pk=int(id)))
    data.pk=None
    data.interfaceResult='2'
    data.save()
    return HttpResponseRedirect('/app/interface_config')
#跳转到执行页面
def interface_request(request,id):
    menu_app=ProjectConfigure.objects.filter(businessName=u'APP组').values('ProjectName').distinct()
    menu_bigdata=ProjectConfigure.objects.filter(businessName=u'大数据服务组').values('ProjectName').distinct()
    id=int(id)
    data=Interface_add.objects.filter(id=id)
    return render(request, 'web/interface_request.html',{'data':data,'menu_bigdata':menu_bigdata,'menu_app':menu_app})
#执行接口get和post
def interface_post(request):
    if request.method=='POST':
        id=request.POST['id']
        print id
        datas=Interface_add.objects.filter(id=int(id))
        for item in datas:
            data2=item.interfaceBody
            headersdb=item.interfaceHead
            url=item.interfaceAdress
    #    取出数据类型是Unicode
    #    print type(headersdb),headersdb
        headersdb2=headersdb.encode('utf-8')#Unicode转为str
    #    print type(eval(headersdb2)),headersdb2,eval(headersdb2)
    #    print type(json.loads(headers.encode('utf-8'))),json.loads(headers.encode('utf-8'))
        headers =eval(headersdb2)#str转为dict，为了urllib2.Request准备请求头{'Content-Type': 'application/json'}
        data_json=eval(data2.encode('utf-8'))
        print type(headers),headers
        if headers['Content-type']=='application/json':
            data_json=json.dumps(data_json)
        url=url.encode('utf-8')
        if request.FILES.has_key('file'):
            file=request.FILES['file']
            filename=handle_uploaded_file(request.FILES['file'])
            files={'file': open(filename, 'rb')}
            response=requests.post(url,data=data_json,files=files)
        else:
            response=requests.post(url,headers=headers,data=data_json)
    else:
        id=request.GET['id']
        url=request.GET['url']
        url=url.encode('utf-8')
        data_json={}
        if request.GET.has_key('body'):
            param=request.GET['body']
            data_json=eval(param.encode('utf-8'))
            print data_json
        response=requests.get(url,params=data_json)
    if(response.status_code==200):
            Interface_add.objects.filter(id=int(id)).update(interfaceResult='1')
    else:
            Interface_add.objects.filter(id=int(id)).update(interfaceResult='0')
    return HttpResponse(response)
#接口细分页面
def consultation(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    # return HttpResponse(u"调试测试")
#    data = InterfaceConfigure.objects.filter(businessName=u"咨询业务").order_by("-id")
    name=request.GET['name']
    datas=Interface_add.objects.filter(business=name).order_by('-id')[:20]
    menu_app=ProjectConfigure.objects.filter(businessName=u'APP组').values('ProjectName').distinct()
    menu_bigdata=ProjectConfigure.objects.filter(businessName=u'大数据服务组').values('ProjectName').distinct()
    try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
        page = int(request.GET.get("page",1))
        if page < 1:
            page = 1
    except ValueError:
            page = 1
    paginator = Paginator( datas,10)   # 设置books在每页显示的数量，这里为2
    try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
         data = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        data = paginator.page(paginator.num_pages)
    return render(request, 'web/Consultation.html', locals())
#细分页面搜索
def search(request):
    menu_app=ProjectConfigure.objects.filter(businessName=u'APP组').values('ProjectName').distinct()
    menu_bigdata=ProjectConfigure.objects.filter(businessName=u'大数据服务组').values('ProjectName').distinct()
    if request.method=='POST':
        interfaceName=request.POST['interfaceName']
        responsible=request.POST['responsible']
        name=request.POST['projectname']
        datas=Interface_add.objects.filter(interfaceName__icontains=interfaceName,responsible__icontains=responsible,business__icontains=name).order_by('-id')
        try:                     #如果请求的页码少于1或者类型错误，则跳转到第1页
            page = int(request.GET.get("page",1))
            if page < 1:
                page = 1
        except ValueError:
            page = 1
        paginator = Paginator( datas,10)   # 设置books在每页显示的数量，这里为2
        try:                     #跳转到请求页面，如果该页不存在或者超过则跳转到尾页
            data = paginator.page(page)
        except(EmptyPage,InvalidPage,PageNotAnInteger):
            data = paginator.page(paginator.num_pages)
        return render(request, 'web/Consultation.html',locals())
    else:
        return HttpResponse('get...')
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
    if request.method=="POST":
        data=request.POST
        print data
        return HttpResponse("一直大黄狗")
#    id=request.POST['id']
#    urldata=request.POST['url']
#    para1=request.POST['header']
#    para2= request.POST['body']
#    payload=json.loads(para2)
#    print payload
#    print type(payload)
#    responsedata=requests.post(urldata,data=payload)
#    id=int(id)
#    data=Interfaceqqu.objects.filter(id=id)
#    print id
#    return render(request, 'web/interface_exe.html',{"data":json.dumps(responsedata.json())},RequestContext(request))
    else:
     return render(request, 'web/interface_exe.html')#,{"responsedata":responsedata.text,"data":data}

#删除接口
@csrf_exempt
def interface_delete_qu(request,id):
    entry = get_object_or_404(Interfaceqqu, pk=int(id))
    entry.delete()
    return HttpResponseRedirect('/app/interface_config_qu')

def handle_uploaded_file(f):
    file_name = ""
    try:
        path = "media/file" + time.strftime('/%Y/%m/%d/%H/%M/%S/')
        if not os.path.exists(path):
            os.makedirs(path)
            file_name = path + f.name
            destination = open(file_name, 'wb+')
            for chunk in f.chunks():
                destination.write(chunk)
            destination.close()
    except Exception, e:
        print e
    return file_name