#!/usr/bin/env python2.7
#coding: utf-8
"""
============================================================================
Author: yonghuo.x
LastChange: 2016-12-23
History:
        2017-03-27: 添加用户和部门管理功能.
        2017-03-28: 密码功能. 
        2017-04-14: api权限管理.
============================================================================
"""
from django.shortcuts import render,render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext

from django.core import serializers

from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from forms import LoginForm, userForm, deptForm, newPasswordForm
from menuAuth.forms import menuForm

from models import department, myUser
from tastypie.models import ApiKey
from menuAuth.models import menu

from ht_cmdb.settings import AUTH_KEY
from lib.send import sendEmail

import time
import hashlib
import json
# Create your views here.
'''登陆处理'''

#获取用户所拥有权限，根据部门权限和个人权限组合而成
def getAuth(user):
    try:
        deptAuth = user.department.auth.all()
        userAuth = user.auth.all()
        uniqUserAuth = [a for a in userAuth if a not in deptAuth]
        userMenuAuth = []
        for d in deptAuth:
            userMenuAuth.append(d)
        for u in uniqUserAuth:
            userMenuAuth.append(u)
    
        data = serializers.serialize('json',userMenuAuth)
        data = json.loads(data)
        data = [d for d in data]
        return data
    except:
        pass

def user_login(request):
    if request.method == "POST":
        if len(request.POST.get('next')) > 0:
            _next = request.POST.get('next')
        else:
            _next = "/"
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                data = myUser.objects.get(username=username)
                if data.is_staff and data.is_active and data.availabity == 1:
                    _user = authenticate(username=username, password=password)
                    auth_login(request, _user)
                    userAuth = getAuth(data)
                    request.session['menuAuth'] = userAuth
                    return HttpResponseRedirect(_next)
            except Exception as e:
                import traceback; e= traceback.print_exc();
                print e
                return render_to_response('accounts/login.html', locals(), context_instance=RequestContext(request))
    
    return render_to_response('accounts/login.html', locals(), context_instance=RequestContext(request))

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')
'''登陆处理结束'''

'''部门管理'''
@login_required
def deptList(request):
    listOrAddTag = ['department','accounts', 'departmentAdd']
    deptList = department.objects.filter(availabity=1)
    return render_to_response('accounts/deptList.html',locals(),context_instance=RequestContext(request))

@login_required
def deptAdd(request):
    listOrAddTag = ['department','accounts', 'departmentAdd']
    data = deptForm()
    if request.method == 'POST':
        post = request.POST
        data = deptForm(post)
        departmentName = post.get('departmentName')
        if not department.objects.filter(departmentName=departmentName,availabity=1):
            if data.is_valid():
                data.save()
                smg = u'%s添加成功！' % departmentName
        else:
            emg = u'%s已存在。'% departmentName
    return render_to_response('accounts/deptAdd.html',locals(),context_instance=RequestContext(request))

@login_required
def deptEdit(request):
    deptId = request.GET.get('id')
    dept = get_object_or_404(department, id=deptId)
    data = deptForm(instance=dept)
    if request.method == 'POST':
        data = deptForm(request.POST, instance=dept)
        if data.is_valid():
            data.save()
            return HttpResponseRedirect('/accounts/departmentList')
    return render_to_response('accounts/deptEdit.html', locals(), context_instance=RequestContext(request))

@login_required
def deptDel(request):
    _id = request.GET.get('id')
    dept = department.objects.filter(id=_id)
    dept.update(availabity=int(time.time()))
    return HttpResponseRedirect('/accounts/departmentList')

'''部门管理结束'''

'''用户管理'''
def getToken(userInfo):
    return str(hashlib.sha1('%s%s%s%s' % (userInfo.username, AUTH_KEY, userInfo.id, time.strftime('%Y-%m-%d', time.localtime(time.time())))).hexdigest())

def sendInitMail(host,userInfo):
    try:
        token = getToken(userInfo)
        url = u'http://%s/accounts/newpasswd/?id=%s&token=%s' % (host, userInfo.id, token)
        mail_title = u'运维管理系统初始密码'
        mail_msg = u"""
        Hi,%s:
            请点击以下链接修改密码,此链接当天有效:
                %s
            有任何问题，请随时和运维组联系。
        """ % (userInfo.first_name, url)
        
        sendEmail([userInfo.email], mail_title, mail_msg)
        return True
    except Exception as e:
        #import traceback
        #print traceback.print_exc()
        return False

def sendApiPswMail(user):
    try:
        mail_title = u'运维管理系统API密码'
        mail_msg = u'''
        Hi,%s:
            您的API账号信息如下：
            账号：%s
            密码：%s
            有任何问题，请随时和运维组联系。
        ''' % (user.first_name, user.username, ApiKey.objects.get(user=user).key)
        sendEmail([user.email], mail_title, mail_msg)
        return True
    except:
        return False

@login_required
def userList(request):
    '''用户列表'''
    listOrAddTag = ['user','accounts', 'userAdd']
    users = myUser.objects.filter(availabity__lte=1)
    return render_to_response('accounts/userList.html', locals(), context_instance=RequestContext(request))

@login_required
def userAdd(request):
    listOrAddTag = ['user','accounts', 'userAdd']
    data = userForm()
    if request.method == 'POST':
        post = request.POST
        data = userForm(post)
        username = post.get('username')
        if data.is_valid():
            data.save()
            if post.get('apiAuth'):
                user = myUser.objects.get(username=username,availabity__lte=1)
                ApiKey(user=user).save()
                if not sendApiPswMail(user):
                    emg = u'api密码发送失败。'
            if post.get('EMAIL_PUSH'):
                user = myUser.objects.get(username=username,availabity=1)
                sendInitMail(request.get_host(),user)
            smg = u'用户%s添加成功！' % username
    return render_to_response('accounts/userAdd.html',locals(),context_instance=RequestContext(request))

@login_required
def userEdit(request):
    userId = request.GET.get('id')
    user = get_object_or_404(myUser, id=userId)
    data = userForm(instance=user)
    chkApiAuth = ApiKey.objects.filter(user=user)
    if request.method == 'POST':
        post = request.POST
        data = userForm(post, instance=user)
        if post.get('apiAuth') and not chkApiAuth:
            ApiKey(user=user).save()
            sendApiPswMail(user)
        elif not post.get('apiAuth') and chkApiAuth:
            chkApiAuth.delete()
        if data.is_valid():
            data.save()
            return HttpResponseRedirect('/accounts/userList')
    return render_to_response('accounts/userEdit.html',locals(),context_instance=RequestContext(request))

@login_required
def userDel(request):
    _id = request.GET.get('id')
    user = myUser.objects.filter(id=_id)
    user.update(is_active=False,is_staff=False,availabity=int(time.time()))
    return HttpResponseRedirect('/accounts/userList')

@login_required
def userStatus(request):
    uid = request.GET.get('id')
    user = myUser.objects.get(id=uid)
    if user.is_staff:
        user.is_staff = False
    else:
        user.is_staff = True
    user.save()
    return HttpResponseRedirect('/accounts/userList')

def newPassword(request):
    uid = request.GET.get("id")
    token = request.GET.get('token')
    data = myUser.objects.get(id=uid)
    new_token = getToken(data)
    uf = newPasswordForm()
    if token == new_token and not data.availabity:
    #if token == new_token:
        if request.method == 'POST':
            uf = newPasswordForm(request.POST, instance=data)
            if uf.is_valid():
                password = request.POST.get("newpassword")
                zw = uf.save(commit=False)
                zw.password = make_password(password, None, 'pbkdf2_sha256')
                zw.is_staff = 1
                zw.availabity = 1
                zw.save()
                _user = authenticate(username=data.username, password=password)
                auth_login(request, _user)
                return HttpResponseRedirect('/')
            else:
                emg = uf.errors.as_data().values()[0][0]
        return render_to_response('accounts/newPassword.html', locals(), context_instance=RequestContext(request))
    return render_to_response('404.html', locals(), context_instance=RequestContext(request))

def resetPassword(request):
    if request.method == 'POST':
        post = request.POST
        username = post.get('username')
        email = request.POST.get('email')
        if username and email:
            try:
                user = myUser.objects.get(username=username,email=email,availabity=1)
            except:
                emg = u'不存在该用户,或邮箱不匹配，请填写注册时邮箱。'
                return render_to_response('accounts/resetPassword.html', locals(), context_instance=RequestContext(request))
            user.availabity = 0
            user.save()
            if sendInitMail(request.get_host(),user):
                return HttpResponseRedirect('/')
            else:
                pass
        return render_to_response('404.html', locals(), context_instance=RequestContext(request))


    return render_to_response('accounts/resetPassword.html', locals(), context_instance=RequestContext(request))

'''用户管理结束'''

#部门或用户授权
@login_required
def Auth(request):
    ID = request.GET.get('id')
    model = m = request.GET.get('m')
    if model == 'myUser':
        model = myUser
    elif model == 'dept':
        model = department
    obj = get_object_or_404(model, id=ID)
    menuInfo = menu.objects.filter(availabity=1)
    if request.method == 'POST':
        post = request.POST
        fatherMenu = menuInfo.filter(fatherID=0)
        obj.auth.clear()
        for father in fatherMenu:
            getMenu = post.getlist(str(father.id))
            if getMenu:
                obj.auth.add(father)
                for subMenu in getMenu:
                    obj.auth.add(menuInfo.get(id=subMenu))
        obj.save()
        #print post
        #print post.getlist()
    return render_to_response('accounts/auth.html', locals(), context_instance=RequestContext(request))
