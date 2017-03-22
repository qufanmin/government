#coding:utf-8
from django import forms

class InterfaceForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(InterfaceForm, self).__init__(*args, **kwargs)
    business=forms.CharField(max_length=255,
                             label=u'业务线',
                             required=True,error_messages={'required':u'请输入业务线'},
                             widget=forms.TextInput(
                                 attrs={
                                     'name': "business",
                                     'type': "text",
                                     'id': "business",
                                     'class': "span1-7",
                                     'placeholder': u"业务线",
                                 }
                             ))
    responsible=forms.CharField(max_length=255,label=u'责任人')
    interfaceName=forms.CharField(max_length=255,label=u'接口名称')
    description=forms.CharField(max_length=255,label=u'接口描述')
    methods=forms.CharField(max_length=255,label=u'请求方式')
    IP=forms.CharField(max_length=255,label=u'IP地址')
    interfaceAdress=forms.CharField(max_length=255,label=u'接口路径')
    interfaceBody=forms.CharField(max_length=1000,label=u'接口请求值')
    interfaceDetails=forms.CharField(max_length=255,label=u'接口详细描述')