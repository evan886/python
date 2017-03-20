#!/usr/bin/python
# -*- coding: UTF-8 -*-

#使用range()循环遍历
tuple = (("apple", "banana"),("grape", "orange"),("watermelon",),("grapefruit",))
for i in range(len(tuple)):
    print "tuple[%d] :" % i, "" ,
    for j in range(len(tuple[i])):
        print tuple[i][j], "" ,
    print

#使用map()循环遍历
k = 0
for a in map(None,tuple):
    print "tuple[%d] :" % k, "" ,
    for x in a:
        print x, "" , 
    print
    k += 1