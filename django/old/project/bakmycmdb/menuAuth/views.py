#coding: utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from models import menu
from forms import menuForm

import time

# Create your views here.
'''菜单管理'''
@login_required
def menuAdminAdd(request):
    listOrAddTag = ['menuAdmin','auth','menuAdminAdd']
    data = menuForm()
    print data
    if request.method == 'POST':
        post = request.POST
        data = menuForm(post)
        if data.is_valid():
            data.save()
    return render_to_response('menuAuth/menuAdminAdd.html',locals(),context_instance=RequestContext(request))

@login_required
def menuAdminList(request):
    listOrAddTag = ['menuAdmin','auth','menuAdminAdd']
    menuList = menu.objects.filter(availabity=1).order_by('fatherID')
    return render_to_response('menuAuth/menuAdminList.html',locals(),context_instance=RequestContext(request))

@login_required
def menuAdminEdit(request):
    menuID = request.GET.get('id')
    menuInfo = get_object_or_404(menu, id=menuID, availabity=1)
    data = menuForm(instance=menuInfo)
    if request.method == 'POST':
        data = menuForm(request.POST, instance=menuInfo)
        if data.is_valid():
            data.save()
            return HttpResponseRedirect('/auth/menuAdminList')
    return render_to_response('menuAuth/menuAdminEdit.html',locals(),context_instance=RequestContext(request))

@login_required
def menuAdminDel(request):
    menuID = request.GET.get('id')
    menu.objects.filter(id=menuID).update(availabity=int(time.time()))
    return HttpResponseRedirect('/auth/menuAdminList')
'''菜单管理结束'''

#'''权限分配'''
#@login_required
#def menuAuthList(request):
#    listOrAddTag = ['menuAdmin','auth']
#    
#'''权限分配结束'''