#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 使用readline()读文件
f = open("hello.txt")
while True:
    line = f.readline()
    if line: 
        print line,
    else:
        break
f.close()

# 使用readlines()读文件
f = file('hello.txt')
lines = f.readlines()
for line in lines:   
    print line,
f.close()                   # 关闭文件 

# 使用read()读文件
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

