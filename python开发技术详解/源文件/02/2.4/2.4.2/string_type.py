#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 单引号和双引号的使用是等价
str = "hello world!"
print str
str = 'hello world!'
print str

# 三引号的用法
str = '''he say "hello world!"'''
print str
# 三引号制作doc文档
class Hello:
    '''hello class'''
    def printHello():
        '''print hello world'''
        print "hello world!"
print Hello.__doc__
print Hello.printHello.__doc__

# 转义字符
str = 'he say:\'hello world!\''
print str
# 直接输出特殊字符
str = "he say:'hello world!'"
print str
str = '''he say:'hello world!' '''
print str
    