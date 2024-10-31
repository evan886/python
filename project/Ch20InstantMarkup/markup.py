import sys,re 
from handlers import  *
from rules import  *

class Parser:
    """
   构造函数是 __init__ 方法, A Parser reads a text file, applying rules and controlling a handler.
    """
    def __init__(self,handler):
        self.handler = handler 
        self.rules = []
        self.filters = []
    def addRule(self,rule):
        self.rules.append(rule)
    def addFilter(self,pattern,name):
        def filter(block,hnadler):
            return re.sub(pattern,handler,sub(name),block)
        self.filters.append(filter)

    def parse(self,file):
        self.handler.start('document')
        for block in blocks(file):
            for fileter in self.filters:
                block = filter(block,self.handler)
                for rule in self.rules:
                    if rule.condition(block):
                        last = rule.action(block,self.handler)
                        if last: break 
        self.handler.end('document')

class BasicTextParser(Parser):
    """
    A specific Parser that adds rules and filters in its constructor.
    """
    
        