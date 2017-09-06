from django.shortcuts import render
from datetime import datetime
from django.template.loader import get_template
from django.http import HttpResponse


def index(request):
    template = get_template('index.html')
    now = datetime.now()
    html = template.render(locals())

    return HttpResponse(html)
