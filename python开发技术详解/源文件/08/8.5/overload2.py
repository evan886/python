#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

class Stream:
    def __init__(self, file):
        self.file=file
    
    def __lshift__(self, obj):      # 对运算符<<进行重载
        self.file.write(str(obj))
        return self

class Fruit(Stream):
    def __init__(self, price = 0, file = None):
        Stream.__init__(self, file)
        self.price = price

class Apple(Fruit):
    pass

class Banana(Fruit):
    pass    

if __name__ == "__main__":
    apple = Apple(2, sys.stdout)    # apple对象可作为流输出
    banana = Banana(3, sys.stdout)
    endl = "\n"     
    apple<<apple.price<<endl        
    banana<<banana.price<<endl