#!/usr/bin/python
#-*- coding:utf-8 -*-
'''
lines生成器的作用为在文件的最后追加一个空行
'''
a = [1,2]
#a = [1,2,3,4,5]
#b = ['h1','how are you','how do you do']

def lines(arg):
    for line in arg:yield   line
    yield  '\n'
#    yield  '\n' #可以关闭试一下的
for i in lines(a):
    print i
#for j in lines(b):
#    print j

'''
evan@evanpc:~$ python  lines_generator.py 
1
2
3
4
5


h1
how are you
how do you do


'''