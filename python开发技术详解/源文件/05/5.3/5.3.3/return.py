#!/usr/bin/python
# -*- coding: UTF-8 -*-

# return���
from __future__ import division
def arithmetic(x, y, operator):
    result = {
        "+" : x + y,
        "-" : x - y,
        "*" : x * y,
        "/" : x / y 
    }
    return result.get(operator)     # ���ؼ�����

# û��return���ĺ�������None
def func():
    pass

print func()

# return�󲻴�����
def func():
    return

print func()

# return���ض��ֵ
def func(x, y, z):
    l = [x, y, z]
    l.reverse()
    numbers = tuple(l)
    return numbers

x, y, z = func(0, 1, 2)
print x, y, z
   
# return���ض��ֵ
def func(x, y, z):
    l = [x, y, z]
    l.reverse()
    a, b, c = tuple(l)   
    return a, b, c

x, y, z = func(0, 1, 2)
print x, y, z    

# ���return���
def func(x):
    if x > 0:
        return "x > 0"
    elif x == 0:
        return "x == 0"
    else:
        return "x < 0"

print func(-2)
        
# ���return�����ع�
def func(x):
    if x > 0:
        result = "x > 0"
    elif x == 0:
        result = "x == 0"
    else:
        result = "x < 0"
    return result    

print func(-2)   
    