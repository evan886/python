#/usr/bin/python
#-*- coding:utf-8 -*-
import sys
def lines(file):
    for line in file:yield line
    yield '\n'

for i in lines(sys.stdin):
    if i:
        print i
        print '---'
'''
python util.py < test_input.txt > test_output.txt

hello

---


---
how are you

---
how do you do

---


---
fine
---


---




这里可以注意到hello后面有个换行，然后再是“---”。个人认为原因如下：

首先，test_input.txt实际上是一个list：

test_input = ['hellon','n','how areyoun','how do you don','n','fine']

其次，print打印出的东西自带换行效果：

print ‘1’
print ‘2’

执行效果为：


即先打印出1，然后换行，再打印2，再换行，最后执行结束。

在test_output.txt中也是这样：

先打印’hellon’，然后换行，然后打印‘---’，再打印’n’，再换行，再打印‘---’。。。





'''