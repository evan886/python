from django.conf.urls import include, url

urlpatterns = [
	url(r'^domainNameAdd/', 'domainNameManager.views.domainName_add'),
	url(r'^domainNameList/', 'domainNameManager.views.domainName_list'),
]