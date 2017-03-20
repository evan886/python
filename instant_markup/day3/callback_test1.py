#!/usr/bin/python
# -*- coding:utf-8 -*-
#有 所以 callable 返回  1,2,3  pass 20161126pm
class CalTest:
    def callback(self,prefix,name,*args):
        method = getattr(self,prefix+name,None)
        if callable(method):return method(*args)
    def printSum(self,*arg):
        sum = 0
        for i in arg:
            sum = sum + i
        return sum 
    
a = CalTest();
b = a.callback('print','Sum',1,2,3)
print b
b = a.callback('print', 'Sum')
print b 
 
'''
前传解说
解说
getattr
其中官方文档对getattr()的解释为：
getattr(object, name[, default]) 
Return the value of the namedattribute of object. name must be a string. If the string is the name of one ofthe object's attributes, the result is the value of that attribute. Forexample, getattr(x, 'foobar') is equivalent to x.foobar. If the named attributedoes not exist, default is returned if provided, otherwise AttributeError israised.
也就是说，若对象中有名为name(name必须是一个字符串)的属性，则返回该属性。如果对象中没有该属性，若getattr中提供了default参数，返回提供的default，否则抛出一个AttributeError错误。
********

很明显，若callable中的参数为函数名，则返回True，否则返回False。另外可以看到命令行中func()执行了一次。函数的执行发生在a = func()这一过程中

综上，函数callback(self,prefix, name, *args)的功能为：
在使用callback函数的对象中查询其是否拥有名为’prefix+name’的函数。若有该函数，则调用该函数，并返回该函数的执行结果。(函数名为prefix+name，参数为*args)。


运行结果
6
0

'''         