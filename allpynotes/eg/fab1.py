#!/usr/bin/python
#-*-coding:utf-8 -*-
"""
迭代实现在不太懂呢


def fab(n):
    n1 = 1
    n2 =  1
    n3 = 1

    if n < 1:
        print('输入有错')
        return  -1
    while (n-2) > 0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -=1
    return  n3

result = fab(20)
if result != -1:
    print ("总共有%d对兔子 生了" % result)
"""

"""
13:16 图

递归 分治思想 

14：00 the  end 
"""
def fab(n):
    if n < 1:
        print ("输入有错!")
        return -1
    if n ==1  or n == 2:
        return 1
    else:
        return  fab(n-1)  + fab(n-2)

result = fab(20)
if result != -1:
    print ("总共有%d对兔子 生了" % result)


