from django.conf.urls import include, url
from django.contrib import admin
from myapp.views import about

urlpatterns = [
    # Examples:
    # url(r'^$', 'mynewsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', homepage),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/',about)
]
