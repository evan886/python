#!/usr/bin/python
# -*- coding: UTF-8 -*-
def abstract():       
    raise NotImplementedError("abstract")

class Fruit:                            # 抽象类
    def __init__(self):
        if self.__class__ is Fruit:     # 如果实例化的类是Fruit，则抛出异常
            abstract()
        print "Fruit"

class Apple(Fruit):
    def __init__(self):
        Fruit.__init__(self)            # 调用父类的__init__
        print "Apple"

if __name__ == "__main__":
    apple = Apple()
    #fruit = Fruit()