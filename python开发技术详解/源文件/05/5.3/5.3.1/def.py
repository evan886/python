#!/usr/bin/python
# -*- coding: UTF-8 -*-

# �����Ķ���
from __future__ import division
def arithmetic(x, y, operator):
    result = {
        "+" : x + y,
        "-" : x - y,
        "*" : x * y,
        "/" : x / y 
    }
    return result.get(operator)     # ���ؼ�����

# �����ĵ���
print arithmetic(1, 2, "+")
 

    