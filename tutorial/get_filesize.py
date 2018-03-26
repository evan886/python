#!/usr/bin/python
#-*- coding:utf-8 -*-
import os   , sys
from os.path import join, getsize 

'''
 [2]: from os.path  import join, getsize 
In [6]: mysite=getsize ("keywordargument.py")
In [7]: mb=mysite/float(1024*1024)
获取文件的大小,结果保留两位小数，单位为MB'''

def get_filesize(filename="note"):
    #filepath=unicode(filepath,'utf8')
    #mysize=getsize("filename") # add "" is str 
    mysize=getsize(filename)/(1024*1024)
    return round(mysize,2)

#版本1 　可以的
print get_filesize("/home/evan/iso/windows10.iso")

#版本2  还有问题
#print get_filesize(str(sys.argv[1:]))

