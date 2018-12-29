#coding: utf-8
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from models import dataCenter, asset ,ASSET_TYPE
from configManager.models import config
from project.models import app, appRole,app_roles

from forms import assetForm, idcForm
from django.forms import modelformset_factory

from lib.export_excel import ExcelResponse
from lib.lib import pages

import time
import json
# Create your views here.

"""asset 操作"""
@login_required
def asset_add(request):
    """ 添加主机 """
    listOrAddTag = ['asset','assets', 'assetAdd']
    af = assetForm()
    projectList = app.objects.filter(availabity=1)
    #roleList = appRole.objects.filter(availabity=1)
    configList = config.objects.filter(availabity=1)

    if request.method == 'POST':
        af = assetForm(request.POST)
        ip = request.POST.get('ip')
        if asset.objects.filter(ip=ip, availabity=1):
            emg = u'添加失败, 该IP %s 已存在!' % ip
        elif af.is_valid():
            af.save()
            smg = u'主机%s添加成功!' % ip
        return render_to_response('assets/host_add.html', locals(), context_instance=RequestContext(request))
    return render_to_response('assets/host_add.html', locals(), context_instance=RequestContext(request))

@login_required
def asset_list(request):
    listOrAddTag = ['asset','assets', 'assetAdd']
    cIdc = request.GET.get('change_idc')
    cType = request.GET.get('change_type')
    cProject = request.GET.get('change_project')
    cRole = request.GET.get('change_role')
    keyword = request.GET.get('keyword')

    assetType = ASSET_TYPE
    assets = asset.objects.filter(availabity=1)
    idcs = dataCenter.objects.filter(availabity=1)
    projects = app.objects.filter(availabity=1)
    roles = appRole.objects.filter(availabity=1)
    serverCount = len(assets)
    cvmCount = len(assets.filter(server_type=u'云服务器'))
    dbCount = len(assets.filter(server_type=u'云数据库'))
    redisCount = len(assets.filter(server_type=u'云缓存Redis'))

    if cIdc and cType and cProject and cRole:
        if cIdc == 'all':
            if cType == 'all':
                if cProject =='all':
                    if cRole == 'all':
                        if not keyword:
                            assets = asset.objects.filter(availabity=1)
                        else:
                            assets = asset.objects.filter(ip__contains=keyword, availabity=1)
                    else:
                        if not keyword:
                            assets = asset.objects.filter(role_name__roleid=cRole, availabity=1)
                        else:
                            assets = asset.objects.filter(ip__contains=keyword, role_name__roleid=cRole, availabity=1)
                else:
                    if cRole == 'all':
                        if not keyword:
                            assets = asset.objects.filter(app_name__id=cProject, availabity=1)
                        else:
                            assets = asset.objects.filter(ip__contains=keyword, app_name__id=cProject, availabity=1)
                    else:
                        if not keyword:
                            assets = asset.objects.filter(app_name__id=cProject, role_name__roleid=cRole, availabity=1)
                        else:
                            assets = asset.objects.filter(ip__contains=keyword, app_name__id=cProject, role_name__roleid=cRole, availabity=1)
            else:
                if cProject =='all':
                    if cRole == 'all':
                        if not keyword:
                            assets = asset.objects.filter(server_type=cType, availabity=1)
                        else:
                            assets = asset.objects.filter(ip__contains=keyword, server_type=cType, availabity=1)
                    else:
                        if not keyword:
                            assets = asset.objects.filter(server_type=cType, role_name__roleid=cRole, availabity=1)
                        else:
                            assets = asset.objects.filter(ip__contains=keyword, server_type=cType, role_name__roleid=cRole, availabity=1)
    
                else:
                    if cRole == 'all':
                        if not keyword:
                            assets = asset.objects.filter(server_type=cType, app_name__id=cProject, availabity=1)
                        else:
                            assets = asset.objects.filter(ip__contains=keyword, server_type=cType, app_name__id=cProject, availabity=1)
                    else:
                        if not keyword:
                            assets = asset.objects.filter(server_type=cType, app_name__id=cProject, role_name__roleid=cRole, availabity=1)
                        else:
                            assets = asset.objects.filter(ip__contains=keyword, server_type=cType, app_name__id=cProject, role_name__roleid=cRole, availabity=1)
                    
        else:
            if cType == 'all':
                if cProject =='all':
                    if cRole == 'all':
                        if not keyword:
                            assets = asset.objects.filter(group__id=cIdc, availabity=1)
                        else:
                            assets = asset.objects.filter(ip__contains=keyword, group__id=cIdc, availabity=1)
                    else:
                        if not keyword:
                            assets = asset.objects.filter(group__id=cIdc, role_name__roleid=cRole, availabity=1)
                        else:
                            assets = asset.objects.filter(ip__contains=keyword, group__id=cIdc, role_name__roleid=cRole, availabity=1)
                else:
                    if cRole == 'all':
                        if not keyword:
                            assets = asset.objects.filter(group__id=cIdc, app_name__id=cProject, availabity=1)
                        else:
                            assets = asset.objects.filter(ip__contains=keyword, group__id=cIdc, app_name__id=cProject, availabity=1)
                    else:
                        if not keyword:
                            assets = asset.objects.filter(group__id=cIdc, app_name__id=cProject, role_name__roleid=cRole, availabity=1)
                        else:
                            assets = asset.objects.filter(ip__contains=keyword, group__id=cIdc, app_name__id=cProject, role_name__roleid=cRole, availabity=1)
            else:
                if cProject =='all':
                    if cRole == 'all':
                        if not keyword:
                            assets = asset.objects.filter(group__id=cIdc, server_type=cType, availabity=1)
                        else:
                            assets = asset.objects.filter(ip__contains=keyword, group__id=cIdc, server_type=cType, availabity=1)
                    else:
                        if not keyword:
                            assets = asset.objects.filter(group__id=cIdc, server_type=cType, role_name__roleid=cRole, availabity=1)
                        else:
                            assets = asset.objects.filter(ip__contains=keyword, group__id=cIdc, server_type=cType, role_name__roleid=cRole, availabity=1)
                else:
                    if cRole == 'all':
                        if not keyword:
                            assets = asset.objects.filter(group__id=cIdc, server_type=cType, app_name__id=cProject, availabity=1)
                        else:
                            assets = asset.objects.filter(ip__contains=keyword, group__id=cIdc, server_type=cType, app_name__id=cProject, availabity=1)
                    else:
                        if not keyword:
                            assets = asset.objects.filter(group__id=cIdc, server_type=cType, app_name__id=cProject, role_name__roleid=cRole, availabity=1)
                        else:
                            assets = asset.objects.filter(ip__contains=keyword, group__id=cIdc, server_type=cType, app_name__id=cProject, role_name__roleid=cRole, availabity=1)
        try:
            cIdc = int(cIdc)
        except:
            pass
        try:
            cType = int(cType)
        except:
            pass
        try:
            cProject = int(cProject)
        except:
            pass
        try:
            cRole = int(cRole)
        except:
            pass

    if request.GET.get('download'):
        data = serializers.serialize('json',assets,use_natural_foreign_keys=True, use_natural_primary_keys=True)
        data = json.loads(data)

        data = [[d['fields'] for d in data]]
        #print data
        headers = [[h for h in data[0][0]]]
        #print headers
        sheet_name=[u'asset']
        return ExcelResponse(data, output_name=u'data', headers=headers, is_template=False, sheet_name=sheet_name)

    if request.is_ajax():
        serverCount = len(assets)
        cvmCount = len(assets.filter(server_type=u'云服务器'))
        dbCount = len(assets.filter(server_type=u'云数据库'))
        redisCount = len(assets.filter(server_type=u'云缓存Redis'))
        assets = list(set(assets))
        s_url = request.get_full_path()
        #分页功能
        ontact_list, p, contacts, page_range, current_page, show_first, show_end = pages(assets, request)
        if request.is_ajax():
            return render_to_response('assets/host_search.html', locals(), context_instance=RequestContext(request))

    else:
        s_url = '%s%s' % (request.get_full_path(),'?')
        #分页功能
        ontact_list, p, contacts, page_range, current_page, show_first, show_end = pages(assets, request)
    return render_to_response('assets/host_list.html', locals(), context_instance=RequestContext(request))

@login_required
def asset_edit(request):
    '''修改主机信息'''
    hostID = request.GET.get('id')
    host = get_object_or_404(asset, id=hostID, availabity=1)
    af = assetForm(instance=host)

    projectList = app.objects.filter(availabity=1)
    hostProjectList = host.app_name.filter(availabity=1)
    projects = [p for p in projectList if p not in hostProjectList]
    hostAppID = [a for a in hostProjectList]
    roleList = app_roles.objects.filter(appid__in=hostAppID)
    hostRoleList = host.role_name.all()
    roles = [p for p in roleList if p not in hostRoleList]
    configList = config.objects.filter(availabity=1)
    hostConfigList = host.config.all()
    configs = [c for c in configList if c not in hostConfigList]
    if request.method == 'POST':
        af = assetForm(request.POST, instance=host)
        if af.is_valid():
            af.save()
            smg = u'主机%s修改成功!' % host.ip
            return render_to_response('assets/host_detail.html', locals(), context_instance=RequestContext(request))
    return render_to_response('assets/host_edit.html', locals(), context_instance=RequestContext(request))

@login_required
def asset_detail(request):
    '''主机详细信息'''
    _id = request.GET.get('id')
    host = get_object_or_404(asset, id=_id, availabity=1)
    return render_to_response('assets/host_detail.html', locals(), context_instance=RequestContext(request))

@login_required
def asset_del(request):
    '''删除主机'''
    _id = request.GET.get('id')
    host = asset.objects.filter(id=_id)
    host.update(availabity=int(time.time()))
    return HttpResponseRedirect('/assets/assetList')


"""asset 操作结束"""


"""dataCenter 操作"""
@login_required
def idc_add(request):
    """ 添加IDC """
    listOrAddTag = ['idc','assets','idcAdd']
    if request.method == 'POST':
        init = request.GET.get("init", False)
        uf = idcForm(request.POST)
        if uf.is_valid():
            idc_name = uf.cleaned_data['name']
            idc_area = uf.cleaned_data['area']
            if dataCenter.objects.filter(name=idc_name,area=idc_area,availabity=1):
                emg = u'添加失败, 此IDC %s 已存在!' % idc_name
                return render_to_response('assets/idc_add.html', locals(), context_instance=RequestContext(request))
            uf.save()
            if not init:
                return HttpResponseRedirect('/assets/idcList/')
            else:
                return HttpResponseRedirect('/assets/server/type/add/?init=true')

    else:
        uf = idcForm()
    return render_to_response('assets/idc_add.html', locals(), context_instance=RequestContext(request))

@login_required
def idc_list(request):
    '''数据中心列表'''
    listOrAddTag = ['idc','assets','idcAdd']
    idcs = dataCenter.objects.filter(availabity=1)
    #server_type = Project.objects.all()
    return render_to_response('assets/idc_list.html', locals(), context_instance=RequestContext(request))

@login_required
def idc_edit(request):
    '''修改数据中心信息'''
    idcID = request.GET.get('id')
    idc = get_object_or_404(dataCenter, id=idcID)
    uf = idcForm(instance=idc)
    if request.method == 'POST':
        uf = idcForm(request.POST, instance=idc)
        if uf.is_valid():
            uf.save()
            return HttpResponseRedirect('/assets/idcList/')
    return render_to_response('assets/idc_edit.html', locals(), context_instance=RequestContext(request))

@login_required
def idc_del(request):
    '''删除数据中心'''
    _id = request.GET.get('id')
    idc = dataCenter.objects.filter(id=_id)
    idc.update(availabity=int(time.time()))
    return HttpResponseRedirect('/assets/idcList')
"""dataCenter 操作结束"""