#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" 传递函数"""
def power_seq(func,seq):
    return  [func(i) for i in seq]

def prigfang(x):
    return x ** 2

if __name__ == "__main__":
    num_seq = [111,3,14, 2.91]
    r = power_seq(prigfang,num_seq)
    print(num_seq)
    print(r)
