#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 使用list的reverse()
def reverse(s):    
    li = list(s) 
    li.reverse()
    s = "".join(li)
    return s

print reverse("hello")

# 循环输出反转的字符串
def reverse(s):
    out = ""
    li = list(s) 
    for i in range(len(li), 0, -1):
        out += "".join(li[i-1])
    return out

print reverse("hello")

# 特殊切片反转字符串
def reverse(s):
    return s[::-1]

print reverse("hello")