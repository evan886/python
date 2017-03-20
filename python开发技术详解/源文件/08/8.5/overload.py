#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Fruit:
    def __init__(self, price = 0):
        self.price = price

    def __add__(self, other):           # ���ؼӺ������
        return self.price + other.price

    def __gt__(self, other):            # ���ش��������       
        if self.price > other.price:
            flag = True 
        else:
            flag = False
        return flag   

class Apple(Fruit):
    pass

class Banana(Fruit):
    pass

if __name__ == "__main__":
    apple = Apple(3)
    print "ƻ���ļ۸�", apple.price
    banana = Banana(2)
    print "�㽶�ļ۸�", banana.price
    print apple > banana
    total = apple + banana
    print "�ϼƣ�", total

