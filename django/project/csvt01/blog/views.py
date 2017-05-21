from django.http import HttpResponse
from django.template import loader, Context
from django.shortcuts import render_to_response
'''
def index(req):
        t = loader.get_template('index.html')
        c = Context({}) 
        return HttpResponse(t.render(c))
        return HttpResponse('<h1>hellow welcome </h1>')
'''


def index(req):
    return render_to_response('index.html',{})
