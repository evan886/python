#!/usr/bin/python3
# --*-- coding:utf-8 --*--
def foo():
    def bar():
        print("bar() is running")
    bar() # run bar func
    print("foo() is running")

foo()
