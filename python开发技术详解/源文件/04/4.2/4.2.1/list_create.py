#!/usr/bin/python
# -*- coding: UTF-8 -*-

list = ["apple", "banana", "grape", "orange"]
print list
print list[2]
list.append("watermelon")
list.insert(1, "grapefruit")
print list
list.remove("grape")
print list
#list.remove("a")
print list.pop()
print list

list = ["apple", "banana", "grape", "orange"]
print list[-2]
print list[1:3]
print list[-3:-1]
list = [["apple", "banana"],["grape", "orange"],["watermelon"],["grapefruit"]]
for i in range(len(list)):
    print "list[%d] :" % i, "" ,
    for j in range(len(list[i])):
        print list[i][j], "" ,
    print

