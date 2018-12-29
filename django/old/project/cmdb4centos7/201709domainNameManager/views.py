#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
============================================================================
Author: evan
LastChange: 2017-02-16
History:
============================================================================
"""
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from models import domainName
from forms import domainForm
#import os

from lib.lib import pages
import json
import urllib2
import time

""" by evan 20170928
def updateInfo(dName):
    post_url = 'http://api.freedomainapi.com/?r=whois&apikey=be44837ce806eb803e4b55a433cef288&domain=%s' % dName
    n = 0
    while True:
        n += 1
        if n > 10:
            return False
        r = urllib2.urlopen(post_url)
        a = r.read()
        b = json.loads(a)
        if b['status'] == '0':
            try:
                try:
                    exptresDate = b['date_expires']
                except:
                    exptresDate = ''
                try:
                    nameDistributor = b['contacts'][0]['organization']
                except:
                    nameDistributor = ''
                try:
                    user = b['contacts'][2]['name']
                except:
                    user = ''
                try:
                    organization = b['contacts'][2]['organization']
                except:
                    organization = ''
                try:
                    email = b['contacts'][2]['email']
                except:
                    email = ''
                domainName.objects.filter(name=dName,availabity=1).update(nameDistributor=nameDistributor,
                                                                                exptresDate=exptresDate,
                                                                                user=user,
                                                                                email=email,
                                                                                organization=organization)
            except Exception as e:
                #import traceback
                #print traceback.format_exc()
                return False
            return True
"""

@login_required
def domainName_add(request):
    listOrAddTag = ['domainName','domainNameManager','domainNameAdd']
    df = domainForm()
    print 2
    if request.method == 'POST':
        emg = ''
        smg = 'smg0saved'
        smg2 = 'smg2'
        post = request.POST
        df = domainForm(post)
        print df
        DName = post.get('name')
        print DName
        #df.save() #by evan
        if domainName.objects.filter(name=DName, availabity=1):
            emg = u'添加失败, 该域名 %s 已存在!' % DName

        elif df.is_valid(): ## 如果提交的数据合法
        #else:
            #  测试 得到是我的数据不合法

            df.save()

            smg2='smg20'

            smg = u'域名%s添加成功!' % DName
            #if not updateInfo(DName):
            #    emg = u'获取信息失败!'
            #print smg+'saved'
        return HttpResponse(json.dumps({'emg':emg, 'smg1':smg,'smg2':smg2,}))
    return render_to_response('domainNameManger/domainName_add.html', locals(), context_instance=RequestContext(request))

@login_required
def domainName_evanadd(request):
    listOrAddTag = ['domainName','domainNameManager','domainNameAdd']
    df = domainForm()

    if request.method == 'POST':
        df = domainForm(request.POST)
        DName = request.POST.get('name')

        emg = 'testemg'
        smg = ''
        # 上面两个str 要先定义 不然 local variable 'emg' referenced before assignment
        #post = request.POST

        #df = domainForm(post)
        #DName = post.get('name')
        if domainName.objects.filter(name=DName, availabity=1):
            emg = u'添加失败, 该域名 %s 已存在!' % DName
        elif df.is_valid():
            df.save()
            smg = u'域名%s添加成功!' % DName
            #if not updateInfo(DName):
            #    emg = u'获取信息失败!'
        return HttpResponse(json.dumps({'emg':emg, 'smg':smg}))
        #return render_to_response('domainNameManger/domainName_add.html', locals(), context_instance=RequestContext(request))

    return render_to_response('domainNameManger/domainName_add.html', locals(), context_instance=RequestContext(request))




@login_required
def domainName_list(request):
    listOrAddTag = ['domainName','domainNameManager','domainNameAdd']
    domainNameList = domainName.objects.filter(availabity=1)
    if request.POST:
        post = request.POST
        action = post.get('action')
        DName = post.get('name')
        if action == 'update':
            if updateInfo(DName):
                return HttpResponse(json.dumps({'status':True}))
            else:
                return HttpResponse(json.dumps({'status':False}))
        if action == 'del':
            domainName.objects.filter(name=DName, availabity=1).update(availabity=int(time.time()))
            return HttpResponse(json.dumps({'status':True}))
    ontact_list, p, contacts, page_range, current_page, show_first, show_end = pages(domainNameList, request)
    return render_to_response('domainNameManger/domainName_list.html', locals(), context_instance=RequestContext(request))
