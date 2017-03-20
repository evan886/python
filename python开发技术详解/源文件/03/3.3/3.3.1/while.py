#!/usr/bin/python
# -*- coding: UTF-8 -*-
i = 1
while i > 0:
    i = i + 1
    print i
    
# while循环
numbers = raw_input("输入几个数字，用逗号分隔：").split(",")
print numbers
x = 0
while x < len(numbers):                   
    print numbers[x]
    x += 1

# 带else子句的while循环
x = input("输入x的值：")
i = 0
while(x <> 0):   
    if(x > 0):
        x -= 1
    else:
        x += 1
    i = i + 1
    print "第%d次循环：" %i, x
else:
    print "x等于0：", x
