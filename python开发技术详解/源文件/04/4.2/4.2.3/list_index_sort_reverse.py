#!/usr/bin/python
# -*- coding: UTF-8 -*-

list = ["apple", "grape", "grape", "orange"]
list.remove("grape")
print list

list = ["apple", "banana", "grape", "orange"]
print list.index("grape")
print list.index("orange")
print "orange" in list

list1 = ["apple", "banana"]
list2 = ["grape", "orange"]
list1.extend(list2)
print list1
list3 = ["watermelon"]
list1 = list1 + list3
print list1
list1 += ["grapefruit"]
print list1
list1 = ["apple", "banana"] * 2
print list1

#使用列表的sort方法排序
list = ["banana", "apple", "orange", "grape"]
list.sort()
print "Sorted list:", list
list.reverse()
print "Reversed list:", list

#使用函数sorted排序,返回一个新的列表
list = ["banana", "apple", "orange", "grape"]
for li in sorted(set(list)):
    print li, "" ,