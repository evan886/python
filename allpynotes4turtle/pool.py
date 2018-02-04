#!/usr/bin/python
#-*-coding:utf-8 -*-
class Turtle:
    def __init__(self,x):
        self.num = x
class Fish:
    def __init__(self,x):
        self.num = x
class Pool:
    def __init__(self,x,y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print("the pool has turtle   %d, fish %d") %(self.turtle.num, self.fish.num)

pool =  Pool(1,10)
pool.print_num()

'''
evan@evanpc:~/github/python/allpynotes$ python3  pool.py 
the pool has turtle   %d, fish %d
Traceback (most recent call last):
  File "pool.py", line 18, in <module>
    pool.print_num()
  File "pool.py", line 15, in print_num
    print("the pool has turtle   %d, fish %d") %(self.turtle.num, self.fish.num)
TypeError: unsupported operand type(s) for %: 'NoneType' and 'tuple'
evan@evanpc:~/github/python/allpynotes$ python  pool.py 
the pool has turtle   1, fish 10

'''
