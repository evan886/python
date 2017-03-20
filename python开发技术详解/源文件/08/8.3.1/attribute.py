#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 定义类的属性
class Fruit:
    price = 0                   # 类的属性

    def __init__(self):
        self.color = "red"      # 实例属性
        zone = "China"          # 局部变量
        
if __name__ == "__main__":
    print Fruit.price
    apple = Fruit()
    print apple.color
    Fruit.price = Fruit.price + 10
    print "apple's price:" + str(apple.price)
    banana = Fruit()        
    print "banana's price:" + str(banana.price)


# 访问私有属性
class Fruit:
    def __init__(self):
        self.__color = "red"        # 私有属性
        
if __name__ == "__main__":
    apple = Fruit()
    print apple._Fruit__color
