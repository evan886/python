#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 计算阶乘
def refunc(n):
    i = 1
    if n > 1:                       # 递归的结束判断
        i = n
        n = n * refunc(n-1)         # 递推
    print "%d! =" %i, n
    return n                        # 回归

refunc(5)

# 使用reduce计算阶乘
print "5! =", reduce(lambda x, y: x * y, range(1, 6))
