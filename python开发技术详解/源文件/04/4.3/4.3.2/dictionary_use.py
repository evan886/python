#!/usr/bin/python
# -*- coding: UTF-8 -*-

#�ֵ����ӡ�ɾ�����޸Ĳ���
dict = {"a" : "apple", "b" : "banana", "g" : "grape", "o" : "orange"}
dict["w"] = "watermelon"
del(dict["a"])
dict["g"] = "grapefruit"
print dict.pop("b")
print dict
dict.clear()
print dict

#�ֵ�ı���
dict = {"a" : "apple", "b" : "banana", "g" : "grape", "o" : "orange"}
for k in dict:
    print "dict[%s] =" % k,dict[k]

#�ֵ�items()��ʹ��
dict = {"a" : "apple", "b" : "banana", "c" : "grape", "d" : "orange"} 
#ÿ��Ԫ����һ��key��value��ɵ�Ԫ�飬���б�ķ�ʽ���
print dict.items()

#����items()ʵ���ֵ�ı���
dict = {"a" : "apple", "b" : "banana", "g" : "grape", "o" : "orange"}
for (k, v) in dict.items():
    print "dict[%s] =" % k, v

#����iteritems()ʵ���ֵ�ı���
dict = {"a" : "apple", "b" : "banana", "c" : "grape", "d" : "orange"} 
print dict.iteritems()
for k, v in dict.iteritems():
    print "dict[%s] =" % k, v
for (k, v) in zip(dict.iterkeys(), dict.itervalues()):
    print "dict[%s] =" % k, v
    


#ʹ���б��ֵ���Ϊ�ֵ��ֵ
dict = {"a" : ("apple",), "bo" : {"b" : "banana", "o" : "orange"}, "g" : ["grape","grapefruit"]}
print dict["a"]
print dict["a"][0]
print dict["bo"]
print dict["bo"]["o"]
print dict["g"]
print dict["g"][1]


