#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import division

def append(args=[]):
    if len(args) <= 0:    
        args = []
    args.append(0)
    print args

append()
append([1])
append()

# ������ȱʡ����
def arithmetic(x=1, y=1, operator="+"):
    result = {
        "+" : x + y,
        "-" : x - y,
        "*" : x * y,
        "/" : x / y 
    }
    return result.get(operator)     # ���ؼ�����

print arithmetic(1, 2)
print arithmetic(1, 2, "-")
print arithmetic(y=3, operator="-")
print arithmetic(x=4, operator="-")
print arithmetic(y=3, x=4, operator="-")



# �б���Ϊ��������
def arithmetic(args=[], operator="+"):
    x = args[0]
    y = args[1]
    result = {
        "+" : x + y,
        "-" : x - y,
        "*" : x * y,
        "/" : x / y 
    }
    return result.get(operator)     # ���ؼ�����

print arithmetic([1, 2])

# ���ݿɱ����
def func(*args):    
    print args

func(1, 2, 3)    

# ���ݿɱ����
def search(*t, **d):
    keys = d.keys()
    values = d.values()
    print keys
    print values
    for arg in t: 
        for key in keys: 
            if arg == key:
                print "find:",d[key]

search("one", "three", one="1",two="2",three="3")
        
    


