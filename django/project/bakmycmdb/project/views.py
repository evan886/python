#coding: utf-8
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from models import app, appRole, app_roles
from forms import appForm, appRoleForm

import time
# Create your views here.

def getRoles(request):
    """根据appID获取角色列表"""
    appIdList = request.GET.getlist('appIdList[]')
    type = request.GET.get('type')
    roleList = []
    for appId in appIdList:
        #print appId
        roles = app_roles.objects.filter(appid__id=appId)
        roleList.extend(roles)
        #print appInfo
        #return HttpResponse(appInfo)
    if type == 'edit':
        return render_to_response('assets/host_edit_roles.html', locals(), context_instance=RequestContext(request))
    else:
        return render_to_response('assets/host_add_roles.html', locals(), context_instance=RequestContext(request))


"""app 操作"""
@login_required
def app_add(request):
    """ 添加app """
    listOrAddTag = ['app','app','appAdd']
    af = appForm()
    roleList = appRole.objects.filter(availabity=1)
    if request.method == 'POST':
        af = appForm(request.POST)
        if af.is_valid():
            appName = af.cleaned_data['name']
            if app.objects.filter(name=appName):
                emg = u'添加失败, 已存在 %s !' % appName
            else:
                anotherName = af.cleaned_data['another_name']
                architecture = af.cleaned_data['architecture']
                _app = app.objects.create(name=appName,another_name=anotherName,architecture=architecture)
                for role in af.cleaned_data['roles']:
                    m2 = app_roles(appid=_app,roleid=role)
                    m2.save()
                return HttpResponseRedirect("/app/appList/")

    return render_to_response('project/app_add.html', locals(), context_instance=RequestContext(request))

@login_required
def app_list(request):
    '''应用列表'''
    listOrAddTag = ['app','app','appAdd']
    apps = app.objects.filter(availabity=1)
    return render_to_response('project/app_list.html', locals(), context_instance=RequestContext(request))

@login_required
def app_edit(request):
    '''修改应用信息'''
    appID = request.GET.get('id')
    _app = get_object_or_404(app, id=appID)
    af = appForm(instance=_app)
    rolesList = appRole.objects.filter(availabity=1)
    appRoleList = _app.roles.filter(availabity=1)
    roleList = [r for r in rolesList if r not in appRoleList]
    if request.method == 'POST':
        af = appForm(request.POST, instance=_app)
        if af.is_valid():
            #af.save()
            appName = af.cleaned_data['name']
            anotherName = af.cleaned_data['another_name']
            architecture = af.cleaned_data['architecture']
            dataRoles = af.cleaned_data['roles']
            _app = app.objects.filter(id=appID,availabity=1)
            _appRoles = _app[0].roles.all()

            delRoles = []
            addRoles = []
            for role in dataRoles:
                if not role in _appRoles:
                    addRoles.append(role)
            for role in _appRoles:
                if not role in dataRoles:
                    delRoles.append(role)
            if delRoles:
                app_roles.objects.filter(appid=_app[0],roleid__in=delRoles).delete()
            _app.update(name=appName,another_name=anotherName,architecture=architecture)
            if addRoles:
                for role in addRoles:
                    m2 = app_roles(appid=_app[0],roleid=role)
                    m2.save()
            return HttpResponseRedirect('/app/appList/')
    return render_to_response('project/app_edit.html', locals(), context_instance=RequestContext(request))
@login_required
def app_del(request):
    '''删除应用'''
    _id = request.GET.get('id')
    _app = app.objects.filter(id=_id)
    _app.update(availabity=int(time.time()))
    return HttpResponseRedirect('/app/appList')

"""app 操作结束"""

"""app role 操作"""
@login_required
def role_add(request):
    """ 添加app角色 """
    listOrAddTag = ['role','app','roleAdd']
    af = appRoleForm()
    if request.method == 'POST':
        af = appRoleForm(request.POST)
        if af.is_valid():
            #appName = af.cleaned_data['app_name']
            roleName = af.cleaned_data['name']
            if appRole.objects.filter(name=roleName, availabity=1):
                emg = u'添加失败, 已存在 %s !' % (roleName)
            else:
                af.save()
                return HttpResponseRedirect("/app/roleList/")

    return render_to_response('project/role_add.html', locals(), context_instance=RequestContext(request))

@login_required
def role_list(request):
    '''应用角色列表'''
    listOrAddTag = ['role','app','roleAdd']
    roles = appRole.objects.filter(availabity=1)
    return render_to_response('project/role_list.html', locals(), context_instance=RequestContext(request))

@login_required
def role_edit(request):
    '''修改角色信息'''
    roleID = request.GET.get('id')
    _role = get_object_or_404(appRole, id=roleID)
    af = appRoleForm(instance=_role)
    if request.method == 'POST':
        af = appRoleForm(request.POST, instance=_role)
        if af.is_valid():
            af.save()
            return HttpResponseRedirect('/app/roleList/')
    return render_to_response('project/role_edit.html', locals(), context_instance=RequestContext(request))

@login_required
def role_del(request):
    '''删除应用'''
    _id = request.GET.get('id')
    _role = appRole.objects.filter(id=_id)
    _role.update(availabity=int(time.time()))
    return HttpResponseRedirect('/app/roleList')


"""app role 操作结束"""