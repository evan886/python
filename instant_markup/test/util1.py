#encoding:utf-8
import re
def lines(file):
    for line in file: yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []

test_input = ['hello\n','\n','how are you\n','how do you do\n','\n','fine']
for i in   blocks(test_input):
        if i:
               print i
               print '---'

'''
http://blog.csdn.net/miaoyunzexiaobao/article/details/43088495

run  result 

hello
---
how are you
how do you do
---
fine
---

strip()的功能为删除字符串中的’\n’等空白字符（只删除首尾的！！！，中间的不删，比如’\nhello\nhello’.strip()，返回的结果为’hello\nhello），并返回结果。append为再之后添加，’’.join的意思是将block中的各元素用’’连接起来,返回连接后的字符串.

执行流程：

首先是line = ’hello\n’，lines.strip()为True，经过if后，block的值为’hello\n’。之后line = ’\n’，if中的line.strip()返回的是False，进入elif，block的值是’hello\n’，返回hello并置空block。之后line = ‘how are you\n’，if中判断为True，block为’how are you\n’，再然后line = ‘how do you do\n’，if中判断仍为True，此时block为：[‘how are you\n’,’how do youdo\n’]，再之后line = ‘\n’，if中判断为False，进入elif，’’.join(block)执行后返回的值为’how are you\nhow do youdo\n’，执行strip()后返回’how are you\nhow do you do’(这里要注意，strip()只删除字符串首尾的空白字符，不会删除字符串中间的)：



一定要有 lines func 不然报错如下 
Traceback (most recent call last):
  File "util1.py", line 12, in <module>
    for i in   blocks(test_input):
  File "util1.py", line 4, in blocks
    for line in lines(file):
NameError: global name 'lines' is not defined



'''
