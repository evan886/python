#!/usr/bin/python   # -*- coding:utf-8 -*-
#生成器，for循环时会依次返回每一行，它只在文件的最后追加了一个空行\n
def lines(file):
    for line in file: yield line 
    yield '\n'
#生成器，for循环时会依次返回文本块组成的函数
def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
            
            
'''
参考 test目录的 详细过程吧 
其中re.sub是正则表达式，将*XXX*替换为：<em>XXX</em>

正则表达式讲解可见：http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html

文本块生成器
这里的两个主要内容是生成器和for...in语法。

首先我们来看lines()方法，参数是文件，然后对文件进行循环，每次读取一行文件，主意这离的yield关键字，这里代表方法是一个生成器，循环的时候到yield我们可以理解成返回一次line内容。文本读完后，yield处是一个'\n'。

blocks()方法就使用了上面的生成器，每次循环取出内容后，对line内容进行判断，如果有值（ if line.strip(): ），去除两边空格，添加到列表中，否则将block列表生成字符串。我们可以看出blocks也是一个生成器，他的实际功能是，从文件中，依次读取出来一个文本块

'''            
