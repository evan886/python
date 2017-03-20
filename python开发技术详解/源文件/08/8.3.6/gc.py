#!/usr/bin/python
# -*- coding: UTF-8 -*-

import gc

class Fruit:
    def __init__(self, name, color):         # 初始化name、color属性
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

class FruitShop:                             # 水果店类
    def __init__(self):
        self.fruits = []

    def addFruit(self, fruit):               # 添加水果
        fruit.parent = self                  # 把Fruit类关联到FruitShop类
        self.fruits.append(fruit)

if __name__ == "__main__":
    shop = FruitShop()
    shop.addFruit(Fruit("apple", "red"))
    shop.addFruit(Fruit("banana", "yellow"))
    print gc.get_referrers(shop )
    del shop 
    print gc.collect()                       # 显示调用垃圾回收器

