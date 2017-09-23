#-*-coding:utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from mysite import views
#from  mysite.views import index

urlpatterns = [
    # Examples:
    #url(r'^$', 'ch07www.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # 'module' object has no attribute 'index'  views.py 中要有index 方法
    #url(r'^$', views.index),
    url(r'^$', views.index),
    url(r'^detail/(\d+)$',views.detail,name='detail-url'),
    url(r'^admin/', include(admin.site.urls)),
]
