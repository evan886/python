#!/usr/bin/python
#-*- coding: utf-8 -*-
import re
phone="2004-959-559 #这·是个外国号码"

#删除字符串中的py 注释
num = re.sub(r'#.*$', "",phone)
print "电话号码:", num 

#删除非数字(-)
num = re.sub(r'\D', "",phone)
print "电话号码是:", num
