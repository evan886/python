#!/usr/bin/python
#-*- coding:utf-8 -*-
import random as r
class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move():
        self.x -=1
        print("我的位置是: ", self.x ,self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("天天吃")
            self.hungry = False
        else:
            print("太撑了吃不下")

fish =Fish()
fish.move()
    
        
