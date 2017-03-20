#!/usr/bin/python
# --*-- coding: utf-8 --*--
import  sys
test = sys.stdin.read()
words= test.split()
wordcount = len(words)
print 'wordcount:', wordcount

'''
In [6]: cat somefile.txt
hello,PYTHON
In [7]: cat somefile.txt | python somescripy.py
wordcount: 1

'''