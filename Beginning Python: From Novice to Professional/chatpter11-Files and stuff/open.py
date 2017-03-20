#!/usr/bin/python
# --*-- coding: utf-8 --*--
f= open('somefile.txt','w')
f.write('hello,')
f.write('PYTHON')
f.close()



#r 是默认的
In [1]: f=open('somefile.txt','r')

In [2]: f.read(4)
Out[2]: 'hell'

In [3]: f.read()
Out[3]: 'o,PYTHON'

'''
  11.2.3 读写行


  专门为防止忘记close 而设计的语句 with 语句

with open("somefile.txt")  as somefile:
    do_someting(somefile)

with 语句可以打开文件并将其赋值到变量上(这里是 somefile)

  '''


