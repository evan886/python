#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ʹ��list��reverse()
def reverse(s):    
    li = list(s) 
    li.reverse()
    s = "".join(li)
    return s

print reverse("hello")

# ѭ�������ת���ַ���
def reverse(s):
    out = ""
    li = list(s) 
    for i in range(len(li), 0, -1):
        out += "".join(li[i-1])
    return out

print reverse("hello")

# ������Ƭ��ת�ַ���
def reverse(s):
    return s[::-1]

print reverse("hello")