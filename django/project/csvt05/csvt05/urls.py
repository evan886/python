from django.conf.urls import include, url
from django.contrib import admin

#by evan
#admin.audodiscover()
#	'module' object has no attribute 'audodiscover'

urlpatterns = [
    # Examples:
    # url(r'^$', 'csvt05.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
