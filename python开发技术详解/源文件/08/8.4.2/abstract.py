#!/usr/bin/python
# -*- coding: UTF-8 -*-
def abstract():       
    raise NotImplementedError("abstract")

class Fruit:                            # ������
    def __init__(self):
        if self.__class__ is Fruit:     # ���ʵ����������Fruit�����׳��쳣
            abstract()
        print "Fruit"

class Apple(Fruit):
    def __init__(self):
        Fruit.__init__(self)            # ���ø����__init__
        print "Apple"

if __name__ == "__main__":
    apple = Apple()
    #fruit = Fruit()