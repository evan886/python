#!/usr/bin/python
# -*- coding:utf-8 -*-
import re
from pprint import pprint
class Handler:
    def sub_emphasis(self,match): #here
        return '<em>%s</em>' % match.group(1)
    #getAttr()用来判断类中是否存在prefix+name的方法，若存在返回prefix+name，否则返回None。'''
    def callback(self,prefix, name,*args):
        method = getattr(self,prefix+name,None)
        #method = getattr(self,sub_emphasis,None) #here 返回什么呢  sub_emphasis 吧 0623am
        if callable(method): return method(*args)
    ##返回方法名subsutitution
    #   name 和 match http://www.yjs001.cn/program/python/22213625267404415054.html
    #pprint(vars(your_object))
    def sub(self,name):
        print "name:"+name #by evan
        def substitution(match):
            #print "match:"  # by evan
            # eg wrapper http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386819879946007bbf6ad052463ab18034f0254bf355000
            result = self.callback('sub_', name, match)
            #嵌套函数参数传递见Python基础教程（第二版）105页。
            print  "name2:"+name #emphasis
            #print match #<_sre.SRE_Match object at 0x7fd1d9794828>
            print(match)
            #result = self.callback('sub_', emphasis, match) #here
            if result is None:
                result = match.group(0)
            return result
        return substitution     #  函数作为返回值   ?  http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0014186131194415d50558b7a1c424f9fb52b84dc9c965c000
a = Handler() #pass
b = re.sub(r'\*(.+?)\*', a.sub('emphasis'),r'This *is* a test')

#把 * * 之间的换成 Handler.sub('emphasis') 也就是 <em></em>
print b
'''
name:emphasis
match:emphasis
This <em>is</em> a test


include /data/apps/nginx/conf/fastcgi.conf;


当时在这了我完全就懵逼了，因为handler.sub('emphasis')返回的明明是一个方法，但是他没有match参数啊。

　　然后仔细看书，书上在前面有这样一句话，re.sub函数可以将第一个函数作为第二个参数。至少笔者觉得这句话写的很奇怪，’第一个函数‘明明要写成第一个参数啊有木有。好吧，不吐槽这些。

　　大概意思就是，re.sub的第二个参数可以是一个函数作为替换式，替换式的参数就是re.sub的第一个参数匹配后返回的正则对象。

　　这下就可以看懂了，我们会去调用sub_emphasis(self,match)，然后match.group(1)表示的实际上是is。关于group(1)大家去看一下，re模块的内容，在这里我就直接告诉你他的内容，就是匹配式(.+?)中的内容

 问题一：
这里re.sub的repl不是一个字符串，而是一个函数，想请教re.sub是如何将match object传递给substitution函数的参数'match'的？可否给出一些之类的简单例子。
我print了一下，发现match是<_sre.SRE_Match object at 0x01A60CA0>
问题二：我看了下re.sub的源代码，
def sub(pattern, repl, string, count=0, flags=0):
    return _compile(pattern, flags).sub(repl, string, count)

可以看到，返回的参数中有一个match='*is*'，这样就为subsitution()提供了match参数。
http://yanyan0108.blog.163.com/blog/static/173747928201551044425589/

程序过程  先 a.sub ==Handler.sub  sub function
运行结果应该是
This <em>is</em> a test



#今天解说
可以看到sub返回了一个新函数，而这个函数会被当成re.sub中的替换函数来使用。
这里书上写错了，应该是
if result is None: result = match.group(0)
不是if result isNone:match.group(0)
因为如果在对象中没找到匹配的函数，result会为None，那么为了不对string做任何修改，应只是返回原来的方法，即return match.group(0)

运行结果应该是
This <em>is</em> a test
******* 20170203am

解说  getattr

其中官方文档对getattr()的解释为：
getattr(object, name[, default]) 
Return the value of the namedattribute of object. name must be a string. If the string is the name of one ofthe object's attributes, the result is the value of that attribute. Forexample, getattr(x, 'foobar') is equivalent to x.foobar. If the named attributedoes not exist, default is returned if provided, otherwise AttributeError israised.

也就是说，若对象中有名为name(name必须是一个字符串)的属性，则返回该属性。如果对象中没有该属性，若getattr中提供了default参数，返回提供的default，否则抛出一个AttributeError错误。

可以看到sub返回了一个新函数，而这个函数会被当成re.sub中的替换函数来使用。
这里书上写错了，应该是
if result is None: result = match.group(0)
不是if result isNone:match.group(0)

因为如果在对象中没找到匹配的函数，result会为None，那么为了不对string做任何修改，应只是返回原来的方法，即return match.group(0)

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
