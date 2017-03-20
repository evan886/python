#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Fruit:
    def __init__(self):
        pass

class HuskedFruit(Fruit):                   # ��Ƥˮ��
    def __init__(self):
        print "initialize HuskedFruit"
    
    def husk(self):                         # ��Ƥ����
        print "husk ..."

class DecorticatedFruit(Fruit):             # ��Ƥˮ��
    def __init__(self):
        print "initialize DecorticatedFruit"

    def decorticat(self):                   # ��Ƥ����
        print "decorticat ..."

class Apple(HuskedFruit):
    pass

class Banana(DecorticatedFruit):
    pass
    
if __name__ == "__main__":
    apple = Apple()
    apple.husk()
    banana = Banana()
    banana.decorticat()