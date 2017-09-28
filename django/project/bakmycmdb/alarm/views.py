#coding: utf-8
#author: yonghuo.x
#since: 2017-04-10

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from models import alarm
from forms import alarmForm, wayChoices
from accounts.models import myUser

import time

# Create your views here.
@login_required
def alarmAdd(request):
    listOrAddTag = ['alarm','alarm', 'alarmAdd']
    af = alarmForm()
    wayList = wayChoices
    userList = myUser.objects.filter(availabity__lte=1)
    if request.method == 'POST':
        post = request.POST
        af = alarmForm(post)
        if af.is_valid():
            af.save()
            smg = u'添加成功！'
        else:
            emg = u'添加失败！'
        return render_to_response('alarm/alarmAdd.html', locals(), context_instance=RequestContext(request))
    return render_to_response('alarm/alarmAdd.html',locals(), context_instance=RequestContext(request))

@login_required
def alarmList(request):
    listOrAddTag = ['alarm','alarm','alarmAdd']
    lists = alarm.objects.filter(availabity=1)
    return render_to_response('alarm/alarmList.html',locals(),context_instance=RequestContext(request))

@login_required
def alarmEdit(request):
    alarmId = request.GET.get('id')
    alarmInfo = get_object_or_404(alarm, id=alarmId, availabity=1)
    af = alarmForm(instance=alarmInfo)
    
    users = myUser.objects.filter(availabity__lte=1)
    objUsers = alarmInfo.user.filter(availabity__lte=1)
    userList = [u for u in users if u not in objUsers]

    objWay = alarmInfo.way.split(',')
    wayList = [w[0] for w in wayChoices if w[0] not in objWay]
    #print objWay
    #print wayList

    if request.method == 'POST':
        post = request.POST
        af = alarmForm(post, instance=alarmInfo)
        if af.is_valid():
            a = af.save()
            a.way = ','.join(post.getlist('way'))
            a.save()
            return HttpResponseRedirect('/alarm/alarmList')
    return render_to_response('alarm/alarmEdit.html',locals(),context_instance=RequestContext(request))

@login_required
def alarmDel(request):
    alarmId = request.GET.get('id')
    alarmInfo = alarm.objects.filter(id=alarmId)
    alarmInfo.update(availabity=int(time.time()))
    return HttpResponseRedirect('/alarm/alarmList')