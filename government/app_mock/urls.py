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
from app_mock import views, memory_views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^api_data/', views.api_data, name='api_data'),
    url(r'^test/', views.test, name='test'),
    url(r'^data/', views.data, name='data'),
    url(r'^interface_config/', views.interface_config, name='interface'),
    url(r'^personnel_config/', views.personnel_config, name='personnel'),
    url(r'^project_config/', views.project_config, name='project'),
    url(r'^memory_management/', memory_views.memory_management, name='memory_management'),
    url(r'^memory_info/', memory_views.memory_info, name='memory_info'),
]
