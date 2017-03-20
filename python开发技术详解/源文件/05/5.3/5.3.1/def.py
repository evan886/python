#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 函数的定义
from __future__ import division
def arithmetic(x, y, operator):
    result = {
        "+" : x + y,
        "-" : x - y,
        "*" : x * y,
        "/" : x / y 
    }
    return result.get(operator)     # 返回计算结果

# 函数的调用
print arithmetic(1, 2, "+")
 

    