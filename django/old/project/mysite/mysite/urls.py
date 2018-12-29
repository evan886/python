from django.conf.urls import include, url
from django.contrib import admin
from learn import  views  as learn_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'bbmysite.views.home', name='home'),
    url(r'^$',learn_views.index),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
