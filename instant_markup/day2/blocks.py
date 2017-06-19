#!/usr/bin/python
# -*- coding:utf-8 -*-
20170619pm  by evan
'''
strip()只删除字符串首尾的空白字符串，不会删除字符串中间的

生成器
http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00138681965108490cb4c13182e472f8d87830f13be6e88000
'''

def lines(file):
    for line in file: yield line
    yield '\n'

def blocks(file):

    block=[]
    for line in lines(file):
        if line.strip(): ##非空行 所以 为
            block.append(line)
        elif block:
            yield  ' '.join(block).strip()  #  if中的line.strip()返回的是False 遇到空白行时（即文本块末尾），且block非空，则连接里面的行，返回相关内容 并置空block
            block=[]

test_input= ['hello\n', '\n', 'how are you\n', 'how do you do\n', '\n','fine']
for i in blocks(test_input):

    if i:
        print i
        print '---'

'''

hello
---
how are you
 how do you do
---
fine
---

首先是line = ’hello\n’，lines.strip()为True，经过if后，block的值为’hello\n’。
之后line = ’\n’，if中的line.strip()返回的是False，进入elif，block的值是’hello\n’，返回hello并置空block。

之后line = ‘how are you\n’，if中判断为True，block为’how are you\n’，再然后line = ‘how do you do\n’，if中判断仍为True，
此时block为：[‘how are you\n’,’how do youdo\n’]，再之后line = ‘\n’，if中判断为False，
进入elif，’’.join(block)执行后返回的值为’how are you\nhow do youdo\n’，
执行strip()后返回’how are you\nhow do you do’(这里要注意，strip()只删除字符串首尾的空白字符，不会删除字符串中间的)：

'''




