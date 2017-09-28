#coding: utf-8
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from models import config
from forms import configForm

import time

# Create your views here.
@login_required
def config_add(request):
    """添加配置文件"""
    listOrAddTag = ['config','configManager', 'configAdd']
    cf = configForm()
    if request.method == 'POST':
        cf = configForm(request.POST)
        if cf.is_valid():
            configName = cf.cleaned_data['config_name']
            if config.objects.filter(config_name=configName):
                emg = u'添加失败，已存在名称为 %s 的配置文件' % configName
            else:
                cf.save()
                return HttpResponseRedirect('/configManager/config_list')
    return render_to_response('config/config_add.html', locals(), context_instance=RequestContext(request))

@login_required
def config_list(request):
    """配置列表"""
    listOrAddTag = ['config','configManager', 'configAdd']
    configList = config.objects.filter(availabity=1)
    return render_to_response('config/config_list.html', locals(), context_instance=RequestContext(request))

@login_required
def config_edit(request):
    '''修改配置信息'''
    configID = request.GET.get('id')
    _config = get_object_or_404(config, id=configID)
    cf = configForm(instance=_config)
    if request.method == 'POST':
        cf = configForm(request.POST, instance=_config)
        if cf.is_valid():
            cf.save()
            return HttpResponseRedirect('/configManager/config_list/')
    return render_to_response('config/config_edit.html', locals(), context_instance=RequestContext(request))

@login_required
def config_del(request):
    '''删除配置'''
    _id = request.GET.get('id')
    _config = config.objects.filter(id=_id)
    _config.update(availabity=int(time.time()))
    return HttpResponseRedirect('/configManager/config_list')