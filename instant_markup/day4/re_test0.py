#!/usr/bin/python
# -*- coding:utf-8 -*-
import re

def Num2A(mathc):
    return 'A'

a = re.sub(r'(\d+)',Num2A,'he123he')
print a
a = re.sub(r'\d+',r'A','he123he')
print a

'''
pass 20170202

\d+ 一个或多个数字 

代码分别通过函数Num2A和字符串A，将字符串hehe123hehe转化为heAhe。

当re.sub的第二个参数repl为函数时，函数的返回值就是想替换的结果。

heAhe
heAhe


先看下re.sub函数

re.sub共有5个参数，不过一般写前三个就好了，即pattern，repl和string

pattern表示正则中的模式字符串，repl可以是字符串，也可以是函数。string为要进行替换的字符串

'''