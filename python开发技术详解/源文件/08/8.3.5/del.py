#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Fruit:
    def __init__(self, color):         # ��ʼ������__color
        self.__color = color
        print self.__color

    def __del__(self):                 # ��������
        self.__color = ""
        print "free ..."

    def grow(self):
        print "grow ..."

if __name__ == "__main__":
    color = "red"
    fruit = Fruit(color)                # �������Ĺ��캯��
    fruit.grow()
    #del fruit                           # ִ����������
