from django.shortcuts import render, render_to_response
from  django.template import  loader, Context, Template
from django.http import HttpResponse
# Create your views here.

def index(req):
    t =loader.get_template('index.html')
    c = Context({'uname':'evan'})
    #html=t.render(c)
    #return HttpResponse(html)
    return HttpResponse(t.render(c))

def index1(req):
    t = Template('<h1>hello {{uname}}</h1>')
    c = Context({'uname':'csvt'})
    return HttpResponse(t.render(c))

def index2(req):
    return render_to_response('index.html',{'uname':'evan02'})
    
    

    
  
    
