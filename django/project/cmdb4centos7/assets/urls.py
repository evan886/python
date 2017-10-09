from django.conf.urls import include, url

urlpatterns = [
    url(r'^assetAdd/$', 'assets.views.asset_add'),
    url(r'^assetList/$', 'assets.views.asset_list'),
    url(r'^host_edit/$', 'assets.views.asset_edit'),
    url(r'^host_detail/$', 'assets.views.asset_detail'),
    url(r'^host_del/$', 'assets.views.asset_del'),
    
    url(r'^idcAdd/$', 'assets.views.idc_add'),
    url(r'^idcList/$', 'assets.views.idc_list'),
    url(r'^idc_edit/$', 'assets.views.idc_edit'),
    url(r'^idc_del/$', 'assets.views.idc_del'),
]