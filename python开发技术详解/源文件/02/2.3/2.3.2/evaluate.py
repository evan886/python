#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 一次新的赋值操作，将创建一个新的变量
x = 1
print id(x)
x = 2
print id(x)

#print y

# 给多个变量赋值
a = (1, 2, 3)
(x, y, z) = a
print "x =", x
print "y =", y
print "z =", z
