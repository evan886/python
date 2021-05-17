#!/usr/bin/python3
# -*- coding: utf-8 -*-
m = {0:0,1:1}

def fib(n):
    if not n  in  m:
        m [n] = fib(n-1) + fib(n-2)
        return  m[n]
if __name__ == "__main__":
    f = fib(10)
    print(f)
