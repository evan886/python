#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ���ļ��Ŀ�ͷ����ȫ�ֱ���
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
# �����ʹ��ȫ�ֱ���
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