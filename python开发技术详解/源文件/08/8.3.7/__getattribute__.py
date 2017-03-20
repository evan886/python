#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Fruit(object):
    def __init__(self, color = "red", price = 0):
        self.__color = color
        self.__price = price
        
    def __getattribute__(self, name):               # 获取属性的方法
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        self.__dict__[name] = value

if __name__ == "__main__":
    fruit = Fruit("blue", 10)
    print fruit.__dict__.get("_Fruit__color")       # 获取color属性
    fruit.__dict__["_Fruit__price"] = 5
    print fruit.__dict__.get("_Fruit__price")       # 获取price属性



    

