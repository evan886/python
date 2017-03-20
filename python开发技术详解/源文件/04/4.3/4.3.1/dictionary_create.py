#!/usr/bin/python
# -*- coding: UTF-8 -*-

#使用字母作为索引
dict = {"a" : "apple", "b" : "banana", "g" : "grape", "o" : "orange"}
print dict
print dict["a"]
#使用数字作为索引
dict = {1 : "apple", 2 : "banana", 3 : "grape", 4 : "orange"}
print dict
print dict[2]
#字典的添加、删除
dict = {1 : "apple", 2 : "banana", 3 : "grape", 4 : "orange"}
del dict[1]
print dict
print dict[2]
#使用元组作为索引
dict = {}
dict[("a","p","p","l","e")] = "apple"
dict[("b","a","n","a","n","a")] = "banana"
print dict
print dict[("a","p","p","l","e")]

print "%s, %(a)s, %(b)s" % {"a":"apple", "b":"banana"}
