#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 在文件的开头定义全局变量
_a = 1
_b = 2
def add():
    global _a
    _a = 3
    return "_a + _b =", _a + _b
def sub():
    global _b
    _b = 4
    return "_a - _b =", _a - _b
print add()
print sub()
# 错误的使用全局变量
_a = 1
_b = 2
def add():
    _a = 3
    return "_a + _b =", _a + _b
def sub():
    _b = 4
    return "_a - _b =", _a - _b
print add()
print sub()    