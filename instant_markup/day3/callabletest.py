#!/usr/bin/python
# -*- coding: utf-8-*-
'''
good 20170621
Python 使用 UTF-8 编码
https://docs.python.org/2/tutorial/interpreter.html#source-code-encoding

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

print callable(a) #True

a = func() #this is a func

print callable(a) #False

a = 1

print callable(a) #False

'''
解说 
很明显，若callable中的参数为函数名，则返回True，否则返回False。
另外可以看到命令行中func()执行了一次。函数的执行发生在a = func()这一过程中

True
this is a func
False
False
'''
