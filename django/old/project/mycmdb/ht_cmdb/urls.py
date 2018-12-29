#coding: utf-8
from django.conf.urls import include, url
from django.contrib import admin

from tastypie.api import Api
from alarm.api import *

v1_api = Api(api_name='v1')
v1_api.register(alarmApi())

urlpatterns = [
    # Examples:
    # url(r'^$', 'ht_cmdb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'dashboard.views.index'),
    url(r'dashboard/', 'dashboard.views.index'),
    #用户管理
    url(r'accounts/', include('accounts.urls')),

    #服务器
    url(r'assets/', include('assets.urls')),
    
    #配置管理
    url(r'configManager/', include('configManager.urls')),
    
    #应用管理
    url(r'app/', include('project.urls')),

    #域名管理
    url(r'domainNameManager/', include('domainNameManager.urls')),

    url(r'alarm/',include('alarm.urls')),
    
    url(r'^api/', include(v1_api.urls)),

    url(r'^auth/', include('menuAuth.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
