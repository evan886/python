#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ���ת���ַ�
path = "hello\tworld\n"
print path
print len(path)  
path = r"hello\tworld\n" 
print path
print len(path)  


# strip()ȥ��ת���ַ�
word = "\thello world\n"
print "ֱ�����:", word
print "strip()�����:", word.strip()
print "lstrip()�����:", word.lstrip()
print "rstrip()�����:", word.rstrip()