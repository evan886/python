from django.conf.urls import include, url

urlpatterns = [
    url(r'^configAdd/$', 'configManager.views.config_add'),
    url(r'^configList/$', 'configManager.views.config_list'),
    url(r'^config_edit/$', 'configManager.views.config_edit'),
    url(r'^config_del/$', 'configManager.views.config_del'),
]
