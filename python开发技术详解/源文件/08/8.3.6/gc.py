#!/usr/bin/python
# -*- coding: UTF-8 -*-

import gc

class Fruit:
    def __init__(self, name, color):         # ��ʼ��name��color����
        self.__name = name
        self.__color = color

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def getName(self):
        return self.__name

    def setColor(self, name):
        self.__name = name

class FruitShop:                             # ˮ������
    def __init__(self):
        self.fruits = []

    def addFruit(self, fruit):               # ���ˮ��
        fruit.parent = self                  # ��Fruit�������FruitShop��
        self.fruits.append(fruit)

if __name__ == "__main__":
    shop = FruitShop()
    shop.addFruit(Fruit("apple", "red"))
    shop.addFruit(Fruit("banana", "yellow"))
    print gc.get_referrers(shop )
    del shop 
    print gc.collect()                       # ��ʾ��������������

