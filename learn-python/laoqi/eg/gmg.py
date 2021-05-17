#!/usr/bin/python3
# -*- coding: utf-8 -*-
def weight(g):
    def cal_mg(m):
        return m * g
    return cal_mg
w = weight(10)
print("w=",w)
mg = w(10)
print("mg=",mg)

g0=9.78046
w0=weight(g0)
mg0=w0(10)
print(mg0)
'''
w= <function weight.<locals>.cal_mg at 0x7f1f2b538e50>
mg= 100

97.8046

所说说run w=weight(10) ,w所引用的是一个func对象(cal_mg) ,而w(10) 则是所引用的func对象cal_mg 传递了一个参数10 也就是m =10, 和原来的g=10 ,算出m*g 并返回结果
不用每次传递两个参数呀


'''
