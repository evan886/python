#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ʹ��readline()���ļ�
f = open("hello.txt")
while True:
    line = f.readline()
    if line: 
        print line,
    else:
        break
f.close()

# ʹ��readlines()���ļ�
f = file('hello.txt')
lines = f.readlines()
for line in lines:   
    print line,
f.close()                   # �ر��ļ� 

# ʹ��read()���ļ�
f = open("hello.txt")
context = f.read() 
print context
f.close()

# read(size)
f = open("hello.txt")
context = f.read(5) 
print context
print f.tell()
context = f.read(5) 
print context
print f.tell()
f.close()

