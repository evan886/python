#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 定义Generator函数
def func(n):
    for i in range(n):
        yield i
# 在for循环中输出
for i in func(3):
    print i
# 使用next()输出
r =  func(3)
print r.next()
print r.next()
print r.next()
#print r.next()


# yield与return区别
def func(n):
    for i in range(n):
        return i
def func2(n):
    for i in range(n):
        yield i

print func(3)
f = func2(3)
print f
print f.next() 
print f.next() 






