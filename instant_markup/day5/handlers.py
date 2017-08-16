#!/usr/bin/python
#-*- coding:utf-8 -*-
class Handler:
    '调用方法的处理类 可参考data4 '
    #判断当前类是否有对应的方法，所有的话则根据提供的额外参数使用对应方法
#     getAttr()用来判断类中是否存在prefix+name的方法，若存在返回prefix+name，否则返回None。http://www.cnblogs.com/isuifeng/p/5839748.html
    def calback(self,prefix,name,*args):
        method = getattr(self,prefix+name,None)
        if callable(method):return  method(*args)

    #callback的辅助方法，前缀就是start，只需要提供方法名即可
    def start(self,name):
        self.calback('start_',name)
    #前缀为end的callback辅助方法
    def end(self,name):
        self.calback('end_',name)

    #返回方法名subsutitution
    def sub(self,name):
        def substitution(match):
            result = self.calback('sub_',name,match)
            if result is None: result = match.group(0)
            return  result
        return substitution

class HTMLRenderer(Handler):
    def start_document(self):
        print '<html>  <head>  <title></title>     </head>  <body>'
    def end_document(self):
        print '</body></html>'
    def start_paragraph(self):
        print '<p>'
    def end_paragraph(self):
         print '</p>'
    def start_heading(self):
         print '<h2>'
    def end_heading(self):
        print '</h2>'
    def start_list(self):
        print '<ul>'
    def end_list(self):
        print '</ul>'
    def start_listitem(self):
        print '<li>'
    def end_listitem(self):
        print '</li>'
    def start_title(self):
        print '<h1>'
    def end_title(self):
        print '</h1>'
    ## 使用Match获得分组信息 http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html
    def sub_emphasis(self,match):
        return '<em>  %s</em>' %match.group(1)
    def sub_url(self,match):
        return  '<a  href=" %s"> %s </a>' % (match.group(1),match.group(1))
    def sub_mail(self,match):
        return  '<a href="mailto: %s"> %s </a>' %(match.group(1),match.group(1))
    def feed(self,data):
        """
        用于输出文本


        :param data:
        :return:
        """
        print data

'''

学习进度 
20170802pm 

这个讲解和课本一样 
https://www.the5fire.com/python-practice-1.html

http://www.cnblogs.com/zxqstrong/p/4676001.html
 20170204am

 http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001374738449338c8a122a7f2e047899fc162f4a7205ea3000

 '''

"""
  handlers.py 被26  20.5.1  处理程序 模块 20170209 base pass   处理从parser调用的方法的对象
执行 是 class Handler，然后再找到对应该的 class HTMLRenderer
 所以 那么调用 handler.callback('start_','paragraph') 就会调用不带参数的hander.start_paragraph。
handlers.py 处理程序模块  处理从parser调用的方法的对象
这个解析器会在每个块的开始部分调用start（）和恩典（）方法，使用合适的块名作为参数。
sub（）方法会用于正则表达式替换中。当使用了'emphasis'
这样的名字调用时，会返回合适的替换函数
    Handle类：
　　1）callback方法负责在给定一个前缀（比如'start_'）和一个名字（比如'paragraph'）后查找正确的方法（比如start_paragraph）,而且使用以 None作为默认值的getattr　　　 方法来完成工作。如果从getattr返回的对象能被调用，那么对象就可以用提供的任意额外的参数调用。比如如果对应的对象是存在的，那么调用                                             handler.callback('start_','paragraph')就会调用不带参数的hander.start_paragraph。
　　2）start和end方法使用各自的前缀start_和end_调用callback方法的助手方法
　　3）sub方法，返回新的函数，这个函数会被当成re.sub中的替换函数来使用
    那么调用 handler.callback('start_','paragraph') 就会调用不带参数的hander.start_paragraph。

getattr()函数是Python自省的核心函数，具体使用大体如下：获取对象引用getattr。  getattr用于返回一个对象属性，或者方法

 2）callable（object）
　　中文说明：检查对象object是否可调用。如果返回True，object仍然可能调用失败；但如果返回False，调用对象ojbect绝对不会成功。
　　注意：类是可调用的，而类的实例实现了__call__()方法才可调用。
　　版本：该函数在python2.x版本中都可用。但是在python3.0版本中被移除，而在python3.2以后版本中被重新添加。

 http://www.cnblogs.com/zxqstrong/p/4676001.html
  callable
http://www.selfrebuild.net/2015/08/25/Python%E6%8B%BE%E9%81%97%20-%20callable()%E5%87%BD%E6%95%B0/
应含义:
    1. 判断 是否 是可调用对象.(返回 true or false)     2. 函数,是可调用的.
所有的 Python 自带的类型,都是可调用的 函数是可调用的.
     Created on 2016年3月8日 @author: evan
    The Parser will call the start() and end() methods at the
    beginning of each block, with the proper block name as a
    parameter. The sub() method will be used in regular expression
    substitution. When called with a name such as 'emphasis', it will
    return a proper substitution function.

Handler类，他有四个方法，其中重点是callback和sub。
callback:两个必须参数，一个额外参数。
getAttr()用来判断类中是否存在prefix+name的方法，若存在返回prefix+name，否则返回None。
　　callable()用来判断方法是否可以调用，若可以调用，则给予参数*args并且调用，*args的含义是额外参数。
start，end是包装了callback的两个方法，不细表。

sub:目的是返回一个函数作为re.sub的替换函数，这样re.sub就不是写死的了。其中定义了一个substitution方法，实际上调用后返回的就是这个方法。他也就是我们后面re.sub中需要用到的替换函数。
这个程序堪称是整个“项目”的基石所在：提供了标签的输出，以及字符串的替换。理解起来也比较简单。

当时在这了我完全就懵逼了，因为handler.sub('emphasis')返回的明明是一个方法，但是他没有match参数啊。
　　然后仔细看书，书上在前面有这样一句话，re.sub函数可以将第一个函数作为第二个参数。至少笔者觉得这句话写的很奇怪，’第一个函数‘明明要写成第一个参数啊有木有。好吧，不吐槽这些。
　　大概意思就是，re.sub的第二个参数可以是一个函数作为替换式，替换式的参数就是re.sub的第一个参数匹配后返回的正则对象。
　　这下就可以看懂了，我们会去调用sub_emphasis(self,match)，然后match.group(1)表示的实际上是is。关于group(1)大家去看一下，re模块的内容，在这里我就直接告诉你他的内容，就是匹配式(.+?)中的内容。
"""