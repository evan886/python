#!/usr/bin/python
# -*- coding: utf-8 -*-

class CalTest:
    def callback(self,prefix,name,*args):
        method = getattr(self,prefix+name,None)
        if callable(method):return method(*args)
    def printSum(self,*arg):
        sum = 0
        for i in arg:
            sum = sum + i
          #就是这个 ，要是后退了 就直接 是0了哦 结果 
        return sum 


     
a = CalTest();
b = a.callback('print','Sum',1,2,3)
print b 
b = a.callback('print', 'Sum')
print b
b = a.callback('print', 'sum')
print b

'''
难点 getattr callback 

6
0
None
测试utf-8
'''


'''           

很明显，若callable中的参数为函数名，则返回True，否则返回False。另外可以看到命令行中func()执行了一次。函数的执行发生在a = func()这一过程中

综上，函数callback(self,prefix, name, *args)的功能为：

在使用callback函数的对象中查询其是否拥有名为’prefix+name’的函数。若有该函数，则调用该函数，并返回该函数的执行结果。(函数名为prefix+name，参数为*args)。
'''






print "测试utf-8"
