#!/usr/bin/python3
# -*- coding: utf-8 -*-
def foo():
    a =1
    def bar():
        b = a +1
        print("b=",b)
    bar()
    print("a=",a)
foo()

''' b= 2
a= 1
'''
