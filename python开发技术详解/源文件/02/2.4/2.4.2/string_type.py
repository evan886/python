#!/usr/bin/python
# -*- coding: UTF-8 -*-

# �����ź�˫���ŵ�ʹ���ǵȼ�
str = "hello world!"
print str
str = 'hello world!'
print str

# �����ŵ��÷�
str = '''he say "hello world!"'''
print str
# ����������doc�ĵ�
class Hello:
    '''hello class'''
    def printHello():
        '''print hello world'''
        print "hello world!"
print Hello.__doc__
print Hello.printHello.__doc__

# ת���ַ�
str = 'he say:\'hello world!\''
print str
# ֱ����������ַ�
str = "he say:'hello world!'"
print str
str = '''he say:'hello world!' '''
print str
    