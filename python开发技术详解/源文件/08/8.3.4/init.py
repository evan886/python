#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Fruit:
    def __init__(self, color):         # ��ʼ������__color
        self.__color = color
        print self.__color

    def getColor(self):
        print self.__color

    def setColor(self, color):
        self.__color = color
        print self.__color

if __name__ == "__main__":
    color = "red"
    fruit = Fruit(color)                # �������Ĺ��캯��
    fruit.getColor()
    fruit.setColor("blue") 
