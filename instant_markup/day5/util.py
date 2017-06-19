#!/usr/bin/python   # -*- coding:utf-8 -*-
#生成器，for循环时会依次返回每一行，它只在文件的最后追加了一个空行\n  #文件末尾追加空行 #生成器，for循环时会依次返回每一行，它只在文件的最后追加了一个空行\n
def lines(file):
    for line in file: yield line 
    yield '\n'
#生成器，for循环时会依次返回文本块组成的函数
def blocks(file):
    block = []
    for line in lines(file):
        if line.strip(): #非空行
            block.append(line)
        elif block:    ##  if中的line.strip()返回的是False 遇到空白行时（即文本块末尾），且block非空，则连接里面的行
            yield ''.join(block).strip()
            block = []
            

#文本块生成器（util.py）

#http://blog.csdn.net/miaoyunzexiaobao/article/details/43114555
'''
参考 test目录的 详细过程吧 
其中re.sub是正则表达式，将*XXX*替换为：<em>XXX</em>

正则表达式讲解可见：http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html

文本块生成器
这里的两个主要内容是生成器和for...in语法。

首先我们来看lines()方法，参数是文件，然后对文件进行循环，每次读取一行文件，主意这离的yield关键字，
这里代表方法是一个生成器，循环的时候到yield我们可以理解成返回一次line内容。文本读完后，yield处是一个'\n'。

blocks()方法就使用了上面的生成器，每次循环取出内容后，对line内容进行判断，如果有值（ if line.strip(): ），
去除两边空格，添加到列表中，否则将block列表生成字符串。我们可以看出blocks也是一个生成器，他的实际功能是，从文件中，依次读取出来一个文本块

strip()的功能为删除字符串中的’\n’等空白字符（只删除首尾的！！！，中间的不删，比如’\nhello\nhello’.strip()，
返回的结果为’hello\nhello），并返回结果。append为再之后添加，’’.join的意思是将block中的各元素用’’连接起来,返回连接后的字符串.

执行流程：

首先是line = ’hello\n’，lines.strip()为True，经过if后，block的值为’hello\n’。之后line = ’\n’，if中的line.strip()返回的是False，进入elif，block的值是’hello\n’，返回hello并置空block。之后line = ‘how are you\n’，if中判断为True，block为’how are you\n’，再然后line = ‘how do you do\n’，if中判断仍为True，此时block为：[‘how are you\n’,’how do youdo\n’]，再之后line = ‘\n’，if中判断为False，进入elif，’’.join(block)执行后返回的值为’how are you\nhow do youdo\n’，执行strip()后返回’how are you\nhow do you do’(这里要注意，strip()只删除字符串首尾的空白字符，不会删除字符串中间的)：



python基础教程笔记—即时标记（详解）
http://www.cnblogs.com/isuifeng/p/5839748.html

'''
