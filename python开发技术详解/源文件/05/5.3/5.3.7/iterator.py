#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ����Generator����
def func(n):
    for i in range(n):
        yield i
# ��forѭ�������
for i in func(3):
    print i
# ʹ��next()���
r =  func(3)
print r.next()
print r.next()
print r.next()
#print r.next()


# yield��return����
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






