#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 使用索引截取子串
word = "world"
print word[4]

# 使用split()获取子串
sentence = "Bob said: 1, 2, 3, 4"
print "使用空格取子串:", sentence.split()
print "使用逗号取子串:", sentence.split(",")
print "使用两个逗号取子串:", sentence.split(",", 2)

# 字符串连接后将分配新的空间
str1 = "a"
print id(str1)
print id(str1 + "b")

# 特殊切片截取子串
str1 = "hello world"
print word[0:3]
print str1[::2]
print str1[1::2]


