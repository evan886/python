#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ʹ��������ȡ�Ӵ�
word = "world"
print word[4]

# ʹ��split()��ȡ�Ӵ�
sentence = "Bob said: 1, 2, 3, 4"
print "ʹ�ÿո�ȡ�Ӵ�:", sentence.split()
print "ʹ�ö���ȡ�Ӵ�:", sentence.split(",")
print "ʹ����������ȡ�Ӵ�:", sentence.split(",", 2)

# �ַ������Ӻ󽫷����µĿռ�
str1 = "a"
print id(str1)
print id(str1 + "b")

# ������Ƭ��ȡ�Ӵ�
str1 = "hello world"
print word[0:3]
print str1[::2]
print str1[1::2]


