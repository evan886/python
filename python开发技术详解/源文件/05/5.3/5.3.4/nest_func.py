#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 嵌套函数
def sum(a, b):
    return a + b
def sub(a, b):
    return a - b
def func():
    x = 1
    y = 2
    m = 3
    n = 4
    return sum(x, y) * sub(m, n)

print func()

# 调用内部函数
def func():
    x = 1
    y = 2
    m = 3
    n = 4
    def sum(a, b):          # 内部函数
        return a + b
    def sub(a, b):          # 内部函数
        return a - b
    return sum(x, y) * sub(m, n)

print func()
        
   
# 内部函数直接使用外层函数的变量
def func():
    x = 1
    y = 2
    m = 3
    n = 4
    def sum():              # 内部函数
        return x + y
    def sub():          # 内部函数
        return m - n
    return sum() * sub()

print func()    