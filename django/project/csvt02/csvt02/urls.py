from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

    # url(r'^$', 'csvt02.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index/$','blog.views.index'),
    url(r'^index1/$','blog.views.index'),
    url(r'^admin/', include(admin.site.urls)),
]
