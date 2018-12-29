from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'csvt06.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/show_author/$', 'blog.views.show_author'),
    url(r'^blog/show_book/$', 'blog.views.show_book'),
]
