#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 算术表达式
from __future__ import division

print "1 + 1 =", 1 + 1
print "2 - 1 =", 2 - 1
print "2 * 3 =", 2 * 3
print "4 / 2 =", 4 / 2
print "1 / 2 =", 1 / 2
print "1 / 2 =", 1.0 / 2.0
print "3 % 2 =", 3 % 2
print "2 ** 3 =", 2 ** 3

# 算术运算的优先级
a = 1
b = 2
c = 3
d = 4
print "a + b * c % d =", a + b * c % d 
print "(a + b) * (c % d) =", (a + b) * (c % d) 

# 关系表达式
print 2 > 1
print 1 <= 2
print 1 == 2
print 1 != 2
print 1 <> 2
# 关系表达式的优先级别
print "1 + 2 < 3 - 1 =>", 1 + 2, "<", 3 - 1, "=>", 1 + 2 < 3 - 1
print "1 + 2 <= 3 > 5 % 2 =>", 1 + 2, "<=", 3, ">", 5 % 2, "=>", 1 + 2 <= 3 > 5 % 2

# 逻辑运算符
print not True
print False and True 
print True and False 
print True or False

# 逻辑表达式的优先级别
print "not 1 and 0 =>", not 1 and 0
print "not (1 and 0) =>", not (1 and 0)
print "(1 <= 2) and False or True =>", (1 <= 2) and False or True
print "(1 <= 2) or 1 > 1 + 2 =>", 1 <= 2, "or", 1 > 2, "=>", (1 <= 2) or (1 < 2)