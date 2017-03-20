#!/usr/bin/python
# -*- coding: UTF-8 -*-

#索引操作
tuple = ("apple", "banana", "grape", "orange")
list = ["apple", "banana", "grape", "orange"]
str = "apple"
print tuple[0]
print tuple[-1]
print list[0]
print list[-1]
print str[0]
print str[-1]

#分片操作
tuple = ("apple", "banana", "grape", "orange")
list = ["apple", "banana", "grape", "orange"]
str = "apple"
print tuple[:3]
print tuple[3:]
print tuple[1:-1]
print tuple[:]
print list[:3]
print list[3:]
print list[1:-1]
print list[:]
print str[:3]
print str[3:]
print str[1:-1]
print str[:] 
