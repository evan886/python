#coding: utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from assets.models import dataCenter, asset
from project.models import app

import json
# Create your views here.

@login_required
def index(request):
    DCCount = []
    DCName = []
    projectName = []
    projectCount = []
    DC = dataCenter.objects.filter(availabity=1)
    for d in DC:
        name = '%s(%s)' % (d.name, d.area)
        DCName.append(name)
        DCAssetInfo = {'value':len(asset.objects.filter(group__name=d.name,group__area=d.area, availabity=1)), 'name':name, 'id':d.id}
        DCCount.append(DCAssetInfo)
    projectList = app.objects.filter(availabity=1)
    for p in projectList:
        name = p.name
        projectName.append(name)
        projectAssetInfo = {'value':len(list(set(asset.objects.filter(app_name__name=name, availabity=1)))), 
                                                                    'name':name,'id':p.id}
        projectCount.append(projectAssetInfo)
    projectName = json.dumps(projectName)
    projectCount = json.dumps(projectCount)
    DCName = json.dumps(DCName)
    DCCount = json.dumps(DCCount)
    return render_to_response('dashboard/index.html', locals(), context_instance=RequestContext(request))