#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 格式化字符串
str1 = "version"
num = 1.0
format = "%s" % str1
print format
format = "%s %d" % (str1, num)
print format

# 带精度的格式化
print "浮点型数字: %f" % 1.25   
print "浮点型数字: %.1f" % 1.25 
print "浮点型数字: %.2f" % 1.254 

# 使用字典格式化字符串
print "%(version)s: %(num).1f" % {"version": "version", "num": 2}

# 字符串对齐
word = "version3.0"
print word.center(20)
print word.center(20, "*")
print word.ljust(0)
print word.rjust(20)
print "%30s" % word


