#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Ƕ�׺���
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

# �����ڲ�����
def func():
    x = 1
    y = 2
    m = 3
    n = 4
    def sum(a, b):          # �ڲ�����
        return a + b
    def sub(a, b):          # �ڲ�����
        return a - b
    return sum(x, y) * sub(m, n)

print func()
        
   
# �ڲ�����ֱ��ʹ����㺯���ı���
def func():
    x = 1
    y = 2
    m = 3
    n = 4
    def sum():              # �ڲ�����
        return x + y
    def sub():          # �ڲ�����
        return m - n
    return sum() * sub()

print func()    