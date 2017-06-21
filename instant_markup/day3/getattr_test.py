#!/usr/bin/python
#-*- coding:utf-8 -*-
class Test:
    def print_hello(self):
        print 'func print_hello work'

a = Test()
b= getattr(a,'print_hello',None)
print b   # 打印func出属性 <bound method Test.print_hello of <__main__.Test instance at 0x7fd2f1785758>>

b() # func print_hello work
#前两行的输出是这个决定的

b = getattr(a, 'NoFunc',None)
print b #print_hello func中没有NoFunc 所以打印出None

'''
<bound method Test.print_hello of <__main__.Test instance at 0x7f7ac1921bd8>>
func print_hello work
None

第一次使用getattr函数时，b尝试获取a中的print_hello函数，从打印结果可看出获取成功之后我们调用了b。

第二次使用getattr函数时，b尝试获取a中的NoFunc函数，从打印结果可看出a中并没有名为NoneFunc的函数，因此b的值为None 


解说
getattr

其中官方文档对getattr()的解释为：
getattr(object, name[, default]) 

Return the value of the namedattribute of object. name must be a string. If the string is the name of one ofthe object's attributes, the result is the value of that attribute. Forexample, getattr(x, 'foobar') is equivalent to x.foobar. If the named attributedoes not exist, default is returned if provided, otherwise AttributeError israised.

也就是说，若对象中有名为name(name必须是一个字符串)的属性，则返回该属性。如果对象中没有该属性，若getattr中提供了default参数，返回提供的default，否则抛出一个AttributeError错误。

'''