file文件处理



==  知识点==
read        读取整个文件
readline    读取下一行
readlines   读取整个文件到一个迭代器以供我们遍历

可以看出直接使用 readlines方法 返回的是一个列表，readline返回的是字符串



我们谈到“文本处理”时，我们通常是指处理的内容。Python 将文本文件的内容读入可以操作的字符串变量非常容易。文件对象提供了三个“读”方法： .read()、.readline() 和 .readlines()。每种方法可以接受一个变量以限制每次读取的数据量，但它们通常不使用变量。 .read() 每次读取整个文件，它通常用于将文件内容放到一个字符串变量中。然而 .read() 生成文件内容最直接的字符串表示，但对于连续的面向行的处理，它却是不必要的，并且如果文件大于可用内存，则不可能实现这种处理。
.readline() 和 .readlines() 非常相似。它们都在类似于以下的结构中使用：

Python .readlines() 示例
fh = open( 'c:\\autoexec.bat')
for line in fh.readlines():
print   line.readline() 和 .readlines()之间的差异是后者一次读取整个文件，象 .read()一样。.readlines()自动将文件内容分析成一个行的列表，该列表可以由 Python 的 for... in ... 结构进行处理。另一方面，.readline()每次只读取一行，通常比 .readlines()慢得多。仅当没有足够内存可以一次读取整个文件时，才应该使用.readline()。
写：

writeline()是输出后换行，下次写会在下一行写。write()是输出后光标在行末不会换行，下次写会接着这行写



== 例子==

In [11]: f = open(r'so')
somefile.txt  sorted

In [11]: f = open(r'somefile.txt')

In [12]: f.read(7)
Out[12]: 'Welcome'

In [13]: f.read(4)
Out[13]: ' to '

In [14]: f.close()


#readline
In [19]: for i in range(3):
    print str(i)+ ': ' +f.readline()
   ....:
0: Welcome to this file

1: There is nothing here except

2: This stupid haiku


#readlines

In [20]: import pprint

In [21]: pprint.pprint(open(r'somefile.txt').readlines())
['Welcome to this file\n',
 'There is nothing here except\n',
 'This stupid haiku']




In [1]: cat somefile.txt
Welcome to this file
There is nothing here except
This stupid haiku
In [2]: f = open (r'somefile.txt','w')

In [3]: f.write('this\nit no\nhaiku')

In [4]: f.close()

In [5]: cat somefile.txt
this
it no
haiku





#我的老报错

>>> f=open('somefile.txt','r')
>>> lines=f.readlines()
>>> f.close()
>>> lines[1]="is a \n"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range



>>> f=open('somefile-11-4.txt','r')
>>> lines=f.readlines()    #将读到的文件内所有的内容放到分配的内存lines里
>>> f.close()
>>> lines[1]='isn't a\n'   #这里必须是双引号，而不是单引号，否则报错
  File "<stdin>", line 1
    lines[1]='isn't a\n'
                  ^
SyntaxError: invalid syntax
>>> lines[1]="isn't a\n"    #在内存的第二行写上字符：isn't a
>>> f=open('somefile-11-4.txt','w')  #以写的方式打开文件
>>> f.writelines(lines)     #将内存lines里的内容写入到文件对象f里
>>> f.close()
>>> f=open('somefile-11-4.txt','r')    #以读的方式打开文件somefile-11-4.txt
>>> print f.read()          #将读出的所有内容打印出来
this
isn't a
haiku
>>>




def readfile(filename):
    ''' Print a file to the standard output. '''
    f = open(filename)
    #f = file(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line
    f.close()


    for filename in sys.argv[1:]:
        readfile(filename)




11.3.4
文件非常大时 readlines 会占用太多的内存 于是可以 fileinput 他只读取需要的文件部份
import fileinput
for line in fileinput.input(filename):
    process(line)


In [1]: import fileinput

In [2]: for line in fileinput.input('somefile.txt'):
   ...:     print line,

   ...:
test



http://blog.csdn.net/jerry_1126/article/details/41926407



11.3.5 文件抚今抚今迭代器
f= open(filename)
for line in f:
    process(line)
f.close



对文件进行迭代而不使用变量 存储文件对象
for line in  open(filename):
    process(line)



sys.stdin是可迭代的
import sys
   for line in sys.stdin:
       process(line)


解包这个要注意一下


http://songzhe.blog.51cto.com/4388159/1185805
http://blog.csdn.net/werm520/article/details/6898473

https://docs.python.org/2/library/stdtypes.html?highlight=readline#file.readline

http://www.cnblogs.com/suancaomei/archive/2012/09/28/2707805.html