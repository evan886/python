from django.conf.urls import include, url

urlpatterns = [
    url(r'^login/$', 'accounts.views.user_login'),
    url(r'^loginout/$', 'accounts.views.user_logout'),
    url(r'^auth/$', 'accounts.views.Auth'),
    url(r'^userList/$', 'accounts.views.userList'),
    url(r'^userAdd/$', 'accounts.views.userAdd'),
    url(r'^userEdit/$', 'accounts.views.userEdit'),
    url(r'^userStatus/$', 'accounts.views.userStatus'),
    url(r'^userDel/$', 'accounts.views.userDel'),

    url(r'^newpasswd/$', 'accounts.views.newPassword'),
    url(r'^resetpass/$', "accounts.views.resetPassword"),
    url(r'^password/$', 'django.contrib.auth.views.password_change', {'template_name': 'accounts/editPassword.html', 'post_change_redirect': '/'}),
    
    url(r'^departmentList/$', 'accounts.views.deptList'),
    url(r'^departmentAdd/$', 'accounts.views.deptAdd'),
    url(r'^departmentEdit/$', 'accounts.views.deptEdit'),
    url(r'^departmentDel/$', 'accounts.views.deptDel'),


]