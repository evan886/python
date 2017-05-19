from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'csvt01.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^blog/index/$','blog.views.index'),
    url(r'^admin/', include(admin.site.urls)),
]
