from django.conf.urls import include, url

urlpatterns = [
    url(r'^menuAdminAdd/$', 'menuAuth.views.menuAdminAdd'),
    url(r'^menuAdminList/$', 'menuAuth.views.menuAdminList'),
    url(r'^menuAdminEdit/$', 'menuAuth.views.menuAdminEdit'),
    url(r'^menuAdminDel/$', 'menuAuth.views.menuAdminDel'),
]