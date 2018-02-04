#!/usr/bin/python
#-*- coding:utf-8 -*-
import random as r
class Fish(object):
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        self.x -=1
#        print("我的位置 : ", self.x ,self.y)
#('\xe6\x88\x91\xe7\x9a\x84\xe4\xbd\x8d\xe7\xbd\xae', 2) 为什么 结果是这样 ，只要带上selff.x 就会 
        print('my place is ',self.x,self.y)

class Goldfish(Fish):
    pass

#class Carp(fish):
class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        #不然move 会报错

        #这是3.0的写法哦
        super().__init__()
        #1.调用未绑定的父类方法
        #Fish.__init__(self)
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("天天吃")
            self.hungry = False
        else:
            print("太撑了吃不下")

fish =Fish()
#fish.move()
#goldfish = Goldfish()
#goldfish.move()

shark = Shark()
#shark.eat()
#shark.eat()
shark.move()

#等于
#Fish.__init__(shark)
#shark.move()
#
    
        
