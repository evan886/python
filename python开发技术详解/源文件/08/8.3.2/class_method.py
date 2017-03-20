#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Fruit:
    price = 0

    def __init__(self):
        self.__color = "red"

    def getColor(self):
        print self.__color
    
    @ classmethod                          # �෽��
    def getPrice(self):
        print self.price

    def __getPrice(self):
        self.price = self.price + 10
        print self.price
    
    count = classmethod(__getPrice)        # �෽��



if __name__ == "__main__":
    apple = Fruit()
    apple.getColor()
    Fruit.count()
    banana = Fruit()
    Fruit.count()
    Fruit.getPrice()
