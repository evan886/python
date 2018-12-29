#!/usr/bin/env python2.7
#coding: utf-8

import json
import urllib2
import time

def checkDomainName(name):
    domainNameInfo = {}
    post_url = 'http://api.freedomainapi.com/?r=whois&apikey=be44837ce806eb803e4b55a433cef288&domain=%s' % name
    r = urllib2.urlopen(post_url)
    a = r.read()
    b = json.loads(a)
    n = 0
    while True:
        n =+ 1
        if b['status'] == '0':
            exptresTime = b['date_expires']
            #print exptresTime
            #print b['contacts'][2]['name']
            #print b['contacts'][2]['full_address']
            #print b['contacts'][2]['organization']
            #print b['contacts'][2]['email']
            break
    exptresTime = time.strptime(exptresTime,'%Y-%m-%d')
    exptresTime = time.mktime(exptresTime)
    #print exptresTime
    nowTime=time.mktime(time.localtime())
    nowTime = time.mktime(time.strptime('2018-11-11','%Y-%m-%d'))
    #print nowTime
    if exptresTime - nowTime <= 2682000.0:
        #print 'bbbbbbb'
