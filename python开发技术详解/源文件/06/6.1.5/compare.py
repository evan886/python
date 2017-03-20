#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 字符串的比较
str1 = 1
str2 = "1"
if str1 == str2:
    print "相同"
else:
    print "不相同"
if str(str1) == str2:
    print "相同"
else:
    print "不相同"

# 比较字符串的开始和结束处
word = "hello world"
print "hello" == word[0:5]
print word.startswith("hello")
print word.endswith("ld", 6)
print word.endswith("ld", 6, 10)
print word.endswith("ld", 6, len(word))