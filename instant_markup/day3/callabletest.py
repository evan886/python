#!/usr/bin/python
# -*- coding: utf-8-*-
'''
Python 使用 UTF-8 编码

#coding=utf-8
# -*- coding: utf-8-*-
原型
 # coding=<encoding name>
  # -*- coding: <encoding name> -*-
 https://www.python.org/dev/peps/pep-0263/

很明显，若callable中的参数为函数名，则返回True，否则返回False。另外可以看到命令行中func()执行了一次。函数的执行发生在a = func()这一过程中

'''

def func():
    print 'this is a func'
a = func 

print callable(a)

a = func()
print callable(a) #False

a = 1
print callable(a)
