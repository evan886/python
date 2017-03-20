#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Fruit(object):
    def __init__(self):
        pass

class HuskedFruit(object):                      # 削皮水果
    def __init__(self):
        print "initialize HuskedFruit"
    
    def husk(self):                             # 削皮方法
        print "husk ..."

class DecorticatedFruit(object):                # 剥皮水果
    def __init__(self):
        print "initialize DecorticatedFruit"

    def decorticat(self):                       # 剥皮方法
        print "decorticat ..."

class Apple(HuskedFruit, Fruit):
    pass

class Banana(DecorticatedFruit, Fruit):
    pass
    
if __name__ == "__main__":
    apple = Apple()
    apple.husk()
    banana = Banana()
    banana.decorticat()