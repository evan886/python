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

# 函数的缺省参数
def arithmetic(x=1, y=1, operator="+"):
    result = {
        "+" : x + y,
        "-" : x - y,
        "*" : x * y,
        "/" : x / y 
    }
    return result.get(operator)     # 返回计算结果

print arithmetic(1, 2)
print arithmetic(1, 2, "-")
print arithmetic(y=3, operator="-")
print arithmetic(x=4, operator="-")
print arithmetic(y=3, x=4, operator="-")



# 列表作为参数传递
def arithmetic(args=[], operator="+"):
    x = args[0]
    y = args[1]
    result = {
        "+" : x + y,
        "-" : x - y,
        "*" : x * y,
        "/" : x / y 
    }
    return result.get(operator)     # 返回计算结果

print arithmetic([1, 2])

# 传递可变参数
def func(*args):    
    print args

func(1, 2, 3)    

# 传递可变参数
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
        
    


