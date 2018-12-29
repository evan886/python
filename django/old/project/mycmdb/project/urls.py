from django.conf.urls import include, url

urlpatterns = [
    url(r'^appAdd/$', 'project.views.app_add'),
    url(r'^appList/$', 'project.views.app_list'),
    url(r'^app_edit/$', 'project.views.app_edit'),
    url(r'^app_del/$', 'project.views.app_del'),
    url(r'^roleAdd/$', 'project.views.role_add'),
    url(r'^roleList/$', 'project.views.role_list'),
    url(r'^role_edit/$', 'project.views.role_edit'),
    url(r'^role_del/$', 'project.views.role_del'),
    url(r'^getRoles/$', 'project.views.getRoles'),
]