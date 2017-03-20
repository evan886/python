#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Fruit:
    price = 0

    def __init__(self):
        self.__color = "red"

    def getColor(self):
        print self.__color
    
    @ classmethod                          # 类方法
    def getPrice(self):
        print self.price

    def __getPrice(self):
        self.price = self.price + 10
        print self.price
    
    count = classmethod(__getPrice)        # 类方法



if __name__ == "__main__":
    apple = Fruit()
    apple.getColor()
    Fruit.count()
    banana = Fruit()
    Fruit.count()
    Fruit.getPrice()
