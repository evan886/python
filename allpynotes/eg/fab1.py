#!/usr/bin/python
#-*-coding:utf-8 -*-
"""
迭代实现在不太懂呢
05:00 开始 
用数据 函数来定义
        1,当n =1
F(n) =  1,当n =2
        F(n-1)+f(n-2), 当n >2
#code start 
def fab(n):
    n1 = 1
    n2 =  1
    n3 = 1

    if n < 1:
        print('输入有错')
        return  -1
    #07:10   一开始假设 n ==5  
    while (n-2) > 0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3  
        n -=1  #循环次数 -1
    return  n3

result = fab(20)
if result != -1:
    print ("总共有%d对兔子 生了" % result)
"""

"""
13:16 图
这个反而好懂一点 
递归 分治思想 

14：00 the  end 
"""
def fab(n):
    if n < 1:
        print ("输入有错!")
        return -1
    if n ==1  or n == 2:
        return 1
    else:
        return  fab(n-1)  + fab(n-2)

result = fab(20)
if result != -1:
    print ("总共有%d对兔子 生了" % result)


