#!/usr/bin/python
#-*- coding:utf-8 -*-
def func():
    print 'this is a func'
a= func
print callable(a)
a = func()
print callable(a)
a=1
print callable(a)

'''
解说 
很明显，若callable中的参数为函数名，则返回True，否则返回False。另外可以看到命令行中func()执行了一次。函数的执行发生在a = func()这一过程中

True
this is a func
False
False
'''