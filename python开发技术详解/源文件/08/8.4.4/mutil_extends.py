#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Fruit(object):
    def __init__(self):
        print "initialize Fruit"
    
    def grow(self):
        print "grow ..."

class Vegetable(object):
    def __init__(self):
        print "initialize Vegetable"    

    def plant(self):
        print "plant ..."

class Watermelon(Vegetable, Fruit):
    pass

if __name__ == "__main__":
    w = Watermelon()
    w.grow()
    w.plant()
