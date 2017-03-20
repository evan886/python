#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Fruit:      
    '''Fruit类'''
    def __str__(self):          # 定义对象的字符串表示
        return self.__doc__

if __name__ == "__main__":
    fruit = Fruit()
    print str(fruit)            # 调用__str__
    print fruit
