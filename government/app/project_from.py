# coding=utf-8
# !/usr/bin/python
__author__ = 'YANGJINHUA963'
from django import forms
from models import ProjectConfigure


class ProjectConfigureForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectConfigureForm, self).__init__(*args, **kwargs)
    businessName = forms.CharField(
        required=True,
        label=u"用户名",
        error_messages={'required': u'请输入业务线名称'},
        widget=forms.TextInput(
            attrs={
                'name': "phoneTextBox",
                'type': "text",
                'id': "phoneTextBox",
                'class': "span1-7",
                'placeholder': u"业务线",
            }
        ),
    )
    ProjectName = forms.CharField(
        required=True,
        label=u"项目名称",
        error_messages={'required': u'请输入项目名称'},
        widget=forms.TextInput(
            attrs={
                'name': "phoneTextBox",
                'type': "text",
                'id': "phoneTextBox",
                'class': "span1-7",
                'placeholder': u"项目",
            }
        ),
    )
    assemblyName = forms.CharField(
        required=True,
        label=u"组件名称",
        error_messages={'required': u'请输入组件名称'},
        widget=forms.TextInput(
            attrs={
                'name': "phoneTextBox",
                'type': "text",
                'id': "phoneTextBox",
                'class': "span1-7",
                'placeholder': u"组件名称",
            }
        ),
    )
    ProjectAdministration = forms.CharField(
        required=True,
        label=u"项目责任人",
        error_messages={'required': u'请输入项目责任人'},
        widget=forms.TextInput(
            attrs={
                'name': "phoneTextBox",
                'type': "text",
                'id': "phoneTextBox",
                'class': "span1-7",
                'placeholder': u"项目责任人",
            }
        ),
    )
    SoftwareAdministration = forms.CharField(
        required=True,
        label=u"开发责任人",
        error_messages={'required': u'请输入开发责任人'},
        widget=forms.TextInput(
            attrs={
                'name': "phoneTextBox",
                'type': "text",
                'id': "phoneTextBox",
                'class': "span1-7",
                'placeholder': u"开发责任人",
            }
        ),
    )
    TestAdministration = forms.CharField(
        required=True,
        label=u"测试责任人",
        error_messages={'required': u'请输入测试责任人'},
        widget=forms.TextInput(
            attrs={
                'name': "phoneTextBox",
                'type': "text",
                'id': "phoneTextBox",
                'class': "span1-7",
                'placeholder': u"测试责任人",
            }
        ),
    )

    class Meta(forms.Form):
        model = ProjectConfigure
        fields = ('businessName', 'ProjectName', 'assemblyName')


class InterfaceConfigureForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InterfaceConfigureForm, self).__init__(*args, **kwargs)
    businessName = forms.CharField(
        required=True,
        label=u"业务名称",
        error_messages={'required': u'业务线名称为空'},
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "name": "input",
                "id": "businessName",
                "class": "span1-5"
            }
        ),
    )
    businessDescribe = forms.CharField(
        required=True,
        label=u"业务描述",
        error_messages={'required': u'业务描述不能为空'},
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "name": "input",
                "id": "businessDescribe",
                "class": "span1-5"
            }
        ),
    )
    InterfaceName = forms.CharField(
        required=True,
        label=u"接口名称",
        error_messages={'required': u'接口名称不能为空'},
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "name": "input",
                "id": "InterfaceName",
                "class": "span1-5"
            }
        ),
    )
#以下是屈凡民添加
class InterfaceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InterfaceForm, self).__init__(*args, **kwargs)
    businessName = forms.CharField(
        required=True,
        label=u"业务名称",
        error_messages={'required': u'业务线名称为空'},
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "name": "input",
                "id": "businessName",
                "class": "span1-5"
            }
        ),
    )