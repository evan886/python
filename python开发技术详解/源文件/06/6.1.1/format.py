#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ��ʽ���ַ���
str1 = "version"
num = 1.0
format = "%s" % str1
print format
format = "%s %d" % (str1, num)
print format

# �����ȵĸ�ʽ��
print "����������: %f" % 1.25   
print "����������: %.1f" % 1.25 
print "����������: %.2f" % 1.254 

# ʹ���ֵ��ʽ���ַ���
print "%(version)s: %(num).1f" % {"version": "version", "num": 2}

# �ַ�������
word = "version3.0"
print word.center(20)
print word.center(20, "*")
print word.ljust(0)
print word.rjust(20)
print "%30s" % word


