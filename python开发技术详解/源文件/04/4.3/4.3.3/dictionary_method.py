#!/usr/bin/python
# -*- coding: UTF-8 -*-

dict = {"a" : "apple", "b" : "banana", "c" : "grape", "d" : "orange"} 
#���key���б�
print dict.keys()
#���value���б�
print dict.values()
#ÿ��Ԫ����һ��key��value��ɵ�Ԫ�飬���б�ķ�ʽ���
print dict.items()

dict = {"a" : "apple", "b" : "banana", "c" : "grape", "d" : "orange"} 
it = dict.iteritems()
print it

#�ֵ���Ԫ�صĻ�ȡ����
dict = {"a" : "apple", "b" : "banana", "c" : "grape", "d" : "orange"} 
print dict
print dict.get("c", "apple")          
print dict.get("e", "apple")
#get()�ĵȼ����
D = {"key1" : "value1", "key2" : "value2"}
if "key1" in D:
    print D["key1"]
else:
    print "None"

#�ֵ�ĸ���
dict = {"a" : "apple", "b" : "banana"}
print dict
dict2 = {"c" : "grape", "d" : "orange"}
dict.update(dict2)
print dict
#udpate()�ĵȼ����
D = {"key1" : "value1", "key2" : "value2"}
E = {"key3" : "value3", "key4" : "value4"}
for k in E:
    D[k] = E[k]
print D
#�ֵ�E�к����ֵ�D�е�key
D = {"key1" : "value1", "key2" : "value2"}
E = {"key2" : "value3", "key4" : "value4"}
for k in E:
    D[k] = E[k]
print D

#����Ĭ��ֵ
dict = {}
dict.setdefault("a")
print dict
dict["a"] = "apple"
dict.setdefault("a","default")
print dict

help(list)

