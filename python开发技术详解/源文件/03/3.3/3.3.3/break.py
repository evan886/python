#!/usr/bin/python
# -*- coding: UTF-8 -*-

# break语句
x = input("输入x的值：")
y = 0
for y in range(0, 100):
    if x == y:
        print "找到数字：", x
        break
else:
    print "没有找到"