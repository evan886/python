#!/usr/bin/python
# -*- coding: UTF-8 -*-

#ʹ����ĸ��Ϊ����
dict = {"a" : "apple", "b" : "banana", "g" : "grape", "o" : "orange"}
print dict
print dict["a"]
#ʹ��������Ϊ����
dict = {1 : "apple", 2 : "banana", 3 : "grape", 4 : "orange"}
print dict
print dict[2]
#�ֵ����ӡ�ɾ��
dict = {1 : "apple", 2 : "banana", 3 : "grape", 4 : "orange"}
del dict[1]
print dict
print dict[2]
#ʹ��Ԫ����Ϊ����
dict = {}
dict[("a","p","p","l","e")] = "apple"
dict[("b","a","n","a","n","a")] = "banana"
print dict
print dict[("a","p","p","l","e")]

print "%s, %(a)s, %(b)s" % {"a":"apple", "b":"banana"}
