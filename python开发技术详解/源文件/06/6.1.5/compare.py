#!/usr/bin/python
# -*- coding: UTF-8 -*-

# �ַ����ıȽ�
str1 = 1
str2 = "1"
if str1 == str2:
    print "��ͬ"
else:
    print "����ͬ"
if str(str1) == str2:
    print "��ͬ"
else:
    print "����ͬ"

# �Ƚ��ַ����Ŀ�ʼ�ͽ�����
word = "hello world"
print "hello" == word[0:5]
print word.startswith("hello")
print word.endswith("ld", 6)
print word.endswith("ld", 6, 10)
print word.endswith("ld", 6, len(word))