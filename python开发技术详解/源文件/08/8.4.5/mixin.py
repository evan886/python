#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Fruit(object):
    def __init__(self):
        pass

class HuskedFruit(object):                      # ��Ƥˮ��
    def __init__(self):
        print "initialize HuskedFruit"
    
    def husk(self):                             # ��Ƥ����
        print "husk ..."

class DecorticatedFruit(object):                # ��Ƥˮ��
    def __init__(self):
        print "initialize DecorticatedFruit"

    def decorticat(self):                       # ��Ƥ����
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