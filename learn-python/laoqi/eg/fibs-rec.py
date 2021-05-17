#!/usr/bin/python3
# -*- coding: utf-8 -*-

def fib(n):
    """
    This is fibnacci by recursion
    """
    if  n ==0:
        reuturn 0
    elif n ==1:
        return 1
    else:
        return  fib(n-1) + fib(n-2)
if __name__ == "__main__":
    f = fib(10)
    print(f)
