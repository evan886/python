#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Fruit:
    def __init__(self, price = 0):
        self.price = price

    def __add__(self, other):           # 重载加号运算符
        return self.price + other.price

    def __gt__(self, other):            # 重载大于运算符       
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
    print "苹果的价格：", apple.price
    banana = Banana(2)
    print "香蕉的价格：", banana.price
    print apple > banana
    total = apple + banana
    print "合计：", total

