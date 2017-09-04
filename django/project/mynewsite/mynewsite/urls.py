from django.conf.urls import include, url
from django.contrib import admin
from myapp.views import about, listing ,disp_detail, index


urlpatterns = [
    # Examples:
    # url(r'^$', 'mynewsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^about/', about),
    url(r'^about/[0|2|3]/$', about),

    url(r'^list/([0-9a-zA-Z]+)/$', disp_detail),
    #url(r'^/([0-9a-zA-Z]+)/$', disp_detail),
    url(r'^list/$', listing),
]
