#!/usr/bin/python
#-*-  coding:utf-8 -*-
def calc(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum 
 
result = calc(1,2,3)
temp = calc()
print result 
print temp 
'''
上面结果为
6
0


也就是说，带*的参数代表一个数量可变的参数(长度可为0)。其具体讲解见链接：
定义可变参数和定义list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001374738449338c8a122a7f2e047899fc162f4a7205ea3000

'''