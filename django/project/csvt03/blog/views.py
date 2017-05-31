#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from  blog.models import Employee
# Create your views here.

def index(req):
    emps = Employee.objects.all()
    return render_to_response('index.html',{'emps':emps})

#render_to_response
