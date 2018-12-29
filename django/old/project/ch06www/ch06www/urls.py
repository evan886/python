from django.conf.urls import include, url
from django.contrib import admin
from  mysite import views
from  mysite.views import index

urlpatterns = [
    # Examples:
    # url(r'^$', 'ch06www.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',index),
    url(r'^$', views.index),
    url(r'^(\d{1})/$', views.index, name='tv-url'),
    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
]
