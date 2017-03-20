#!/usr/bin/python
# -*- coding:utf-8 -*-
import re
class Handler:
    def sub_emphasis(self,match):
        return '<em>%s</em>' % match.group(1)
    ''' getAttr()用来判断类中是否存在prefix+name的方法，若存在返回prefix+name，否则返回None。'''
    def callback(self,prefix, name,*args):
        method = getattr(self,prefix+name,None)
        if callable(method): return method(*args)
    ##返回方法名subsutitution
    def sub(self,name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            #result = self.callback('sub_', emphasis, match)
            if result is None:
                result = match.group(0)
            return result
        return substitution
        
a = Handler()
b = re.sub(r'\*(.+?)\*', a.sub('emphasis'),r'This *is* a test')
#把 * * 之间的换成 Handler.sub('emphasis') 也就是 <em></em>
print b

'''
程序过程  先 a.sub ==Handler.sub  sub function
运行结果应该是
This <em>is</em> a test
******* 20170203am

http://www.cnblogs.com/isuifeng/p/5839748.html



    处理程序模块 调用方法的处理类,解析器在每个块的开始和结束部分调用start(),end()方法，使用合适的块名作为参数。sub()方法用于  正则表达式替换中，它会返回合适的替换函数

很明显，若callable中的参数为函数名，则返回True，否则返回False。
判断当前类是否有对应的方法，所有的话则根据提供的额外参数使用对应方法

也就是说，若对象中有名为name(name必须是一个字符串)的属性，则返回该属性。如果对象中没有该属性，若getattr中提供了default参数，返回提供的default，否则抛出一个AttributeError错误。
很明显，若callable中的参数为函数名，则返回True，否则返回False。另外可以看到命令行中func()执行了一次。函数的执行发生在a = func()这一过程中
***********

p327
，函数callback(self,prefix, name, *args)的功能为：
在使用callback函数的对象中查询其是否拥有名为’prefix+name’的函数。若有该函数，则调用该函数，并返回该函数的执行结果。(函数名为prefix+name，参数为*args)。

ln 13 调用 def sub_emphasis 


#今天解说
可以看到sub返回了一个新函数，而这个函数会被当成re.sub中的替换函数来使用。
这里书上写错了，应该是
if result is None: result = match.group(0)
不是if result isNone:match.group(0)
因为如果在对象中没找到匹配的函数，result会为None，那么为了不对string做任何修改，应只是返回原来的方法，即return match.group(0)

运行结果应该是
This <em>is</em> a test

'''

'''
import re
class Handler:
    def sub_emphasis(self,match):
        return '<em>%s</em>' % match.group(1)
    def callback(self,prefix, name,*args):
        method = getattr(self,prefix+name,None)
        if callable(method): return method(*args)
    def sub(self,name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None: result = match.group(0)
            return result
        return substitution

a = Handler()
a = re.sub(r'\*(.+?)\*', a.sub('emphasis'),r'This *is* a test')
print a
'''