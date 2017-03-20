#!/usr/bin/python
# -*- coding: UTF-8 -*-

# return语句
from __future__ import division
def arithmetic(x, y, operator):
    result = {
        "+" : x + y,
        "-" : x - y,
        "*" : x * y,
        "/" : x / y 
    }
    return result.get(operator)     # 返回计算结果

# 没有return语句的函数返回None
def func():
    pass

print func()

# return后不带参数
def func():
    return

print func()

# return返回多个值
def func(x, y, z):
    l = [x, y, z]
    l.reverse()
    numbers = tuple(l)
    return numbers

x, y, z = func(0, 1, 2)
print x, y, z
   
# return返回多个值
def func(x, y, z):
    l = [x, y, z]
    l.reverse()
    a, b, c = tuple(l)   
    return a, b, c

x, y, z = func(0, 1, 2)
print x, y, z    

# 多个return语句
def func(x):
    if x > 0:
        return "x > 0"
    elif x == 0:
        return "x == 0"
    else:
        return "x < 0"

print func(-2)
        
# 多个return语句的重构
def func(x):
    if x > 0:
        result = "x > 0"
    elif x == 0:
        result = "x == 0"
    else:
        result = "x < 0"
    return result    

print func(-2)   
    