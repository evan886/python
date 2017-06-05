#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django import forms
from django.http import HttpResponse

class UserForm(forms.Form):
    name = forms.CharField()


def register(req):
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            print form.cleaned_data
            return  HttpResponse('ok')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})

'''
问题
The view didn't return an HttpResponse object. It returned None instead

原因  果真是缩进问题

我先用下面这个试过了

def register(req):
    form = UserForm()
    return render_to_response('register.html', {'form': form})

'''






