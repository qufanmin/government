#coding:utf-8
from django import forms
from app.models import *

class InterfaceForm(forms.ModelForm):
    business=forms.ModelChoiceField(queryset=ProjectConfigure.objects.all(),required=True,error_messages={'required':u'请选择接口'})
#    business=forms.ChoiceField(label=u'业务线')
#    def __init__(self,*args,**kwargs):
#        super(InterfaceForm,self).__init__(*args,**kwargs)
#        self.fields['business'].choices=((item.id,item.ProjectName) for item in ProjectConfigure.objects.all())
    responsible=forms.CharField(max_length=255,label=u'责任人',required=True,error_messages={'required':u'责任人不能为空'})
    interfaceName=forms.CharField(max_length=255,label=u'接口名称',required=True,error_messages={'required':u'接口名称不能为空'})
    description=forms.CharField(max_length=255,label=u'接口描述',required=False)
    methods=forms.ChoiceField(choices=[('', '---------'),('POST', 'POST'),('GET', 'GET'),('DELETE', 'DELETE'),('PUT', 'PUT'),('HEAD', 'HEAD')],label=u'请求方式',required=True,error_messages={'required':u'请求方式不能为空'})
    IP=forms.CharField(max_length=255,label=u'IP地址',required=True,error_messages={'required':u'IP不能为空'})
    interfaceHead=forms.CharField(max_length=100,required=False)
    interfaceAdress=forms.CharField(
        max_length=255,label=u'接口路径',
        required=True,
        error_messages={'required':u'接口路径不能为空','color':'red'},
        widget=forms.Textarea(
        attrs={
            'type':'Textarea',
            'rows':'3',
            'style':'width: 779px; height: 60px'
        }
    ),)
    interfaceBody=forms.CharField(max_length=2000,label=u'接口请求值',required=False,widget=forms.Textarea(
        attrs={
            'type':'Textarea',
            'rows':'3',
            'style':'width: 779px; height: 60px'
        }
    ),)
    interfaceDetails=forms.CharField(max_length=255,label=u'接口详细描述',required=False,widget=forms.Textarea(
        attrs={
            'type':'Textarea',
            'rows':'3',
            'style':'width: 779px; height: 60px'
        }
    ),)
    class Meta:
        model=Interface_add
        fields=['business','responsible','interfaceName','description','methods','IP','interfaceAdress','interfaceBody','interfaceDetails','interfaceHead']