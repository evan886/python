# -*- coding:utf-8 -*-
import sys, re
from handlers import *
from util import *
from rules import *
from bike.logging import Handler

class Parser:
    """
    语法分析器模块 markup.py 调用各个逻辑模块实现文档标记功能  .最后隆重的来看下“语法分析器模块”，这个模块的作用其实就是协调读入的文本和其他模块的关系。在往重点说就是，提供了两个存放“规则”和“过滤器”的列表，这么做的好处就是使得整个程序的灵活性得到了极大的提高，使得规则和过滤器变成的热插拔的方式，当然这个也归功于前面在写规则和过滤器时每一种类型的规则（过滤器）都单独的写成了一个类，而不是用if..else来区分
    添加过滤器前先要创建它。过滤器只是个函数，它对合适的正则表达式应用re.sub，并用handler.sub(name)进行替换
    """       
    def __init__(self,handler):   
        self.handler = Handler
        self.rules = []
        self.fileters = []
    def addRule(self,rule):
        self.rules.append(rule)
    def addFilter(self,pattern,name):
        
        
        def filter(block,handler):
            return re.sub(pattern, handler.sub(name), block)
        self.fileters.append(filter)
    def parse(self,file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.fileters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.codition(block):
                    last = rule.action(block,self.handler)
                    if last: break
        self.handler.end('documet')

class  BasicTextParser(Parser):
    def __init__(self,handler):
        Parser.__init__(self,handler)
        self.addRule(ListRule)
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())
        #三个过滤器了，分别是：强调牌过滤器（用×号标出的），url牌过滤器，email牌过滤器。
        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)','url')
        self.addFilter(r'', name)
        
        
       
        
    