#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 动态添加方法
class Fruit:   
    pass   
  
def grow(self):   
    print "grow ..."  

if __name__ == "__main__":
    Fruit.grow = grow
    fruit = Fruit()   
    fruit.grow()


# 动态更新方法
class Fruit():      
    def grow(self):      
        print "grow ..."  

def add():      
    print "grow ......" 

if __name__ == "__main__":
    fruit = Fruit()      
    fruit.grow()      
    fruit.grow = add
    fruit.grow()   

