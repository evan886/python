#!/usr/bin/env python2.7
#coding: utf-8
#author: yonghuo.x
#since: 2017-04-13

from django.core.mail import send_mail
from ht_cmdb.settings import EMAIL_HOST_USER

def sendEmail(email,title,message):
    try:
        send_mail(title, message, (EMAIL_HOST_USER), email, fail_silently=False)
        return {'code':1,'message':'succeed'}
    except:
        return {'code':2,'message':'send fail'}