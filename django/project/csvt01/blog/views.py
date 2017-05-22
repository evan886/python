#-*- coding:utf-8 -*-
#from django.http import HttpResponse
#from django.template import loader, Context
from django.shortcuts import render_to_response

class Person(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def say(self):
        return  "I am " + self.name
#变量定义
def index(req):
    #user = {'name':'tom', 'age':23, 'sex':'male'}
    user = Person ('max',33,'male')
    book_list = [ 'python','java','php','web']
    return render_to_response('index.html',{'title':'my page','user':user,'book_list':book_list})
