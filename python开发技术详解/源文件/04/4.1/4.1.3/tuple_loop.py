#!/usr/bin/python
# -*- coding: UTF-8 -*-

#ʹ��range()ѭ������
tuple = (("apple", "banana"),("grape", "orange"),("watermelon",),("grapefruit",))
for i in range(len(tuple)):
    print "tuple[%d] :" % i, "" ,
    for j in range(len(tuple[i])):
        print tuple[i][j], "" ,
    print

#ʹ��map()ѭ������
k = 0
for a in map(None,tuple):
    print "tuple[%d] :" % k, "" ,
    for x in a:
        print x, "" , 
    print
    k += 1