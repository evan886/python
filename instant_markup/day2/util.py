#!/usr/bin/python
#--*-- coding:utf-8 --*--
'''
re.sub是正则表达式，将*XXX*替换为：<em>XXX</em>

. 换行\n 外的任意字符
+ > = 1
?  匹配前一个字符0次或1次

In [1]: r=r'\*(.+?)\*'
In [2]: import re

In [3]: re.findall(r,'**')
Out[3]: []

In [4]: re.findall(r,'*9*')
Out[4]: ['9']

In [5]: re.findall(r,'*97*')
Out[5]: ['97']





'''
import sys, re

def lines(file):
    for line  in file: yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ' '.join(block).strip()
            block=[]

print '<html><head><title>... </title><body>'
title = True
for block in blocks(sys.stdin):
    block= re.sub(r'\*(.+?)\*', r'<em>\1</em>',block)
    if title:
        print '<h1>'
        print block
        print  '</h1>'
        title = False
    else:
        print '<p>'
        print block
        print '</p>'

print '</body></html>'