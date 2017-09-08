#-*-coding: utf-8 -*-
from django.shortcuts import render
from datetime import datetime
from django.template.loader import get_template
from django.http import HttpResponse


def index(request, tvno='0'):
    tv_list = [{'name': 'CCTV News', 'tvcode': 'c5ZGQoK16QM'},
               {'name': 'CCTV中文国际', 'tvcode': 'mOUYiBsccVc'}, ]

    template = get_template('index.html')
    now = datetime.now()
    hour = now.timetuple().tm_hour
    tvno = tvno
    tv = tv_list[int(tvno)]
    html = template.render(locals())

    return HttpResponse(html)


def index0(request):
    template = get_template('index.html')
    now = datetime.now()
    html = template.render(locals())

    return HttpResponse(html)
