#!/usr/bin/python
# -*- coding: UTF-8 -*-

tuple = ("apple", "banana", "grape", "orange")
print tuple[-1]
print tuple[-2]
tuple2 = tuple[1:3]
tuple3 = tuple[0:-2]
tuple4 = tuple[2:-2]
print tuple2
print tuple3
print tuple4

fruit1 = ("apple", "banana")
fruit2 = ("grape", "orange")
tuple = (fruit1, fruit2)
print tuple
print "tuple[0][1] =",tuple[0][1]
print "tuple[1][1] =",tuple[1][1]
#print tuple[1][2]

#打包
tuple = ("apple", "banana", "grape", "orange")
#解包
a, b, c, d = tuple
print a, b, c, d


    

