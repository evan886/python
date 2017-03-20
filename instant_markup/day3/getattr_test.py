#!/usr/bin/python
#-*- coding:utf-8 -*-
class Test:
    def print_hello(self):
        print 'func print_hello work'
        #pirnt 'func  print_hello work'
      
a = Test()
 
b= getattr(a,'pirnt_hello',None)
print b 
b()
b = getattr(a, 'NoFunc',None)
print b 

'''
解说
getattr

其中官方文档对getattr()的解释为：
getattr(object, name[, default]) 

Return the value of the namedattribute of object. name must be a string. If the string is the name of one ofthe object's attributes, the result is the value of that attribute. Forexample, getattr(x, 'foobar') is equivalent to x.foobar. If the named attributedoes not exist, default is returned if provided, otherwise AttributeError israised.

也就是说，若对象中有名为name(name必须是一个字符串)的属性，则返回该属性。如果对象中没有该属性，若getattr中提供了default参数，返回提供的default，否则抛出一个AttributeError错误。

'''