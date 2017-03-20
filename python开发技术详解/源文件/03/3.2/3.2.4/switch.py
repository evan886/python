#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 使用字典实现switch语句
from __future__ import division
x = 1
y = 2
operator = "/"
result = {
	"+" : x + y,
	"-" : x - y,
	"*" : x * y,
	"/" : x / y 
}
print result.get(operator)          
