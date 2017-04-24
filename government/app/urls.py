"""government URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from app import views, memory_views, dataservice_views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^api_data/', views.api_data, name='api_data'),
    url(r'^test/', views.test, name='test'),
    url(r'^data/', views.data, name='data'),
    url(r'^personnel_config/', views.personnel_config, name='personnel'),
    url(r'^personnel_add/', views.personnel_add, name='personnel_add'),
    url(r'^personnel_update-(?P<id>\d+)/$', views.personnel_update, name='personnel_update'),
    url(r'^personnel_delete-(?P<id>\d+)/$', views.personnel_delete, name='personnel_delete'),
    url(r'^memory_management/', memory_views.memory_management, name='memory_management'),
    url(r'^memory_info/', memory_views.memory_info, name='memory_info'),
    url(r'^project_add/', dataservice_views.project_add, name='project_add'),
    url(r'^project_update-(?P<id>\d+)/$', dataservice_views.project_update, name="project_update"),
    url(r'^project_config/', dataservice_views.project_config, name='project'),
    url(r'^project_delete-(?P<id>\d+)/$', dataservice_views.project_delete, name="project_delete"),
    url(r'^interface_config/', memory_views.interface_config, name='interface'),
    url(r'^interface_add/', dataservice_views.interface_add, name='interface_add'),
    url(r'^interface_delete-(\d+)/$', dataservice_views.interface_delete, name='interface_delete'),
    url(r'^interface_edit-(?P<id>\d+)/$', dataservice_views.interface_edit, name="interface_edit"),
    url(r'^interface_copy-(?P<id>\d+)/$', dataservice_views.interface_copy, name="interface_copy"),
    url(r'^interface_request-(\d+)/$', dataservice_views.interface_request, name='interface_request'),
    url(r'^consultation/', dataservice_views.consultation, name='consultation'),
    url(r'^quotation/', dataservice_views.quotation, name='quotation'),
    url(r'^api_details/', dataservice_views.api_details, name='api_details'),
    url(r'^interface_post/$', dataservice_views.interface_post, name='interface_post'),
    url(r'^search/$', dataservice_views.search, name='search'),
]
