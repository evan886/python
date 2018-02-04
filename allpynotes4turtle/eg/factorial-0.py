#!/usr/bin/python
#-*-coding:utf-8 -*-
def factorial(n):
    if n == 1:
        return 1
    else:
        return  n * factorial(n-1)

number = int(input('please:'))
result = factorial(number)
print("%d 的阶乘是: %d" %(number,result))



"""
def factorial(n):
    result = n
    for i in range(1,n):
        result *= i

    return result

number = int(input('please:'))
result = factorial(number)
print("%d 的阶乘是: %d" %(number,result))





5 * 1 * 2 * 3 *4 

please:5
5 的阶乘是: 120


阶乘
In [5]: for i in range(1,4):
   ...:     print  (i)
   ...:     
1
2
3

[http://www.10tiao.com/html/383/201608/2247483733/1.html Python计算整数阶乘的几种方法比较]

"""