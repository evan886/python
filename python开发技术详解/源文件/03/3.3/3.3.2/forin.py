#!/usr/bin/python
# -*- coding: UTF-8 -*-

# for in语句
for x in range(-1, 2):
    if x > 0: 
        print "正数：",x
    elif x == 0 : 
        print "零：",x
    else:
        print "负数：",x
else:
    print "循环结束"


# 传统for循环的实现
x = 0
while x < 5:
    print x
    x = x + 2

for x in range(0, 5, 2):
    print x
    
    



    