#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 输出转义字符
path = "hello\tworld\n"
print path
print len(path)  
path = r"hello\tworld\n" 
print path
print len(path)  


# strip()去掉转义字符
word = "\thello world\n"
print "直接输出:", word
print "strip()后输出:", word.strip()
print "lstrip()后输出:", word.lstrip()
print "rstrip()后输出:", word.rstrip()