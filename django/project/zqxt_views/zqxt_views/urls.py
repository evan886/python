#-*- coding:utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from calc import views as calc_views
#from appname

#突然不太明白这个了
urlpatterns = [
    url(r'^$',calc_views.index, name='home'),
    url(r'^add/$',calc_views.add, name='add'),
    url(r'^add/(\d+)/(\d+)/$', calc_views.add2, name='add2'),
    url(r'^admin/', admin.site.urls),
]
