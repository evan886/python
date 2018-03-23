#!/usr/bin/python
#-*- coding:utf-8 -*-
def printhe(name,sex):
    sex_dict = {1:u'先生',2:u'女士'}
    #return  print 'hello %s %s, welcome to python world!' %(name,sex_dict.get(sex,u'先生'))
    mylove= 'hello'+' '+name + '' + sex_dict.get(sex,u'先生')+','+'welcome to python world!'
    #mylove = 5 * 8
    return mylove


    
print printhe('evan',1)
    

