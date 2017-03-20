#!/usr/bin/python
#--*-- coding:utf-8 --*--
"""
start 程序运行从这里开始
同样先看基类Parser,构造函数需要一个handler对象作为参数，以供全局调用，同时初始化了两个列表。
　　addRule和addFilter的目的是向规则和过滤器列表添加元素。
　　parse方法，读取文本文件，循环出每一个文本块，先通过过滤器过滤，然后执行相应规则。
　　我们注意，规则和按照列表依次执行的，他会判断返回值，若为False则不再对文本块执行后续规则了。
　　BasicTextParser类，的构造函数只是在基类的基础上增加了，向规则和过滤器列表添加具体内容的步骤。
　　然后初始化类，并且对文件执行parse方法，即时标记项目完成。
use:  python markup.py <test_input.txt > test_input.html
"""
import  sys, re
from  handlers  import  *
from util  import *
from rules  import  *

class Parser:
    #初始化一些属性 语法分析器
    def __init__(self,handler):
        self.handler = handler
        self.rules = []
        self.filters = []
    #向规则列表中添加规则
    def addRule(self,rule):
        self.rules.append(rule)
    #向过滤器列表中添加过滤器
    def addFilter(self,pattern,name):
        """
     添加过滤器前先要创建它。过滤器只是个函数，它对合适的正则表达式应用re.sub，并用handler.sub(name)进行替换
        """
        #创建过滤器，实际上这里return的是一个替换式
        def filter(block,handler):
            return  re.sub(pattern,handler.sub(name),block)
        self.filters.append(filter)
    #对文件进行处理
    def parse(self,file):
        self.handler.start('document')
        #对文件中的文本块依次执行过滤器和规则
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block,self.handler)
            for rule in self.rules:
                #判断文本块是否符合相应规则，若符合做执行规则对应的处理方法
                if rule.condition(block):
                    last = rule.action(block,self.handler)
                    if last:break
        self.handler.end('document')

class BasicTextParser(Parser):
    def __init__(self,handler):
        Parser.__init__(self,handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())
#三个过滤器，分别是：关于强调的内容，关于URL，关于电子邮件地址
        self.addFilter(r'\*(.+?)\*','emphasis')
        self.addFilter(r'(http://[\.a-zA-Z]+)','url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)','mail')

handler = HTMLRenderer() ##handlers.py
parser =BasicTextParser(handler)
parser.parse(sys.stdin)

#parser.parse(sys.stdin)


'''
start 程序运行从这里开始
前面是实例 . 后面是方法/属性
 python markup.py  < test_input.txt > out.html

 sys.stdin == test_input.txt
 程序开始走的伪代码流程
  parser.parse(sys.stdin) ==>
  BasicTextParser(handler).parse( test_input.txt )   ==>
  BasicTextParser(handler).parse( test_input.txt )   ==>
  BasicTextParser(HTMLRenderer()).parse( test_input.txt )   ==>




   ==>

'''







