#!/usr/bin/python
# --*-- coding:utf-8 --*--
import sys
def readfile(filename):  #从文件中读出文件内容
    '''Print a file to the standard output.'''
    #f = file(filename)
    f = open(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line, # notice comma  分别输出每行内容
    f.close()

#print "sys.argv[0]---------",sys.argv[0]
#print "sys.argv[1]---------",sys.argv[1]
#print "sys.argv[2]---------",sys.argv[2]
# Script starts from here
if len(sys.argv) < 2:
    print 'No action specified.'
    sys.exit()
if sys.argv[1].startswith('--'):
   option = sys.argv[1][2:]
   # fetch sys.argv[1] but without the first two characters
   if option == 'version': #当命令行参数为-- version，显示版本号
      print 'Version 1.2'
   elif option == 'help':
      print '''
           This program prints files to the standard output.
           Any number of files can be specified.
           Options include:
           --version : Prints the version number
           --help    : Display this help'''
   else:
       print 'Unknown option.'
       sys.exit()
else:
    for filename in sys.argv[1:]:  ##当参数为文件名时，传入readfile，读出其内容
        readfile(filename)
    #print "haha"

'''
Sys.argv[]是用来获取命令行参数的，sys.argv[0]表示代码本身文件路径，所以参数从1开始，以下两个例子说明
sys.argv变量是一个字符串的列表。特别地，sys.argv包含了命令行参数 的列表，即使用命令行传递给你的程序的参数。

这里，当我们执行python using_sys.py we are arguments的时候，我们使用python命令运行using_sys.py模块，后面跟着的内容被作为参数传递给程序。Python为我们把它存储在sys.argv变量中。记住，脚本的名称总是sys.argv列表的第一个参数。所以，在这里，'using_sys.py'是sys.argv[0]、'we'是sys.argv[1]、'are'是sys.argv[2]以及'arguments'是sys.argv[3]。注意，Python从0开始计数，而非从1开始。

sys.argv[]是用来获取命令行参数的，sys.argv[0]表示代码本身文件路径;比如在CMD命令行输入 “python  test.py -help”，那么sys.argv[0]就代表“test.py”。sys.startswith() 是用来判断一个对象是以什么开头的，比如在python命令行输入“'abc'.startswith('ab')”就会返回True
注意:sys.argv[1][2:]表示从第二个参数，从第三个字符开始截取到最后结尾，本例结果为:version


evan@evanpc:~/github/python/py4ops$ python arvgtest.py  --version  help
sys.argv[0]--------- arvgtest.py
sys.argv[1]--------- --version
sys.argv[2]--------- help
Version 1.2


https://docs.python.org/2/library/sys.html

#这个为准
http://blog.csdn.net/vivilorne/article/details/3863545

保存为arvgtest.py,我们验证一下：

1）命令行带参数运行：sarvgtest.py --version 输出结果为：version 1.2

2）命令行带参数运行：arvgtest.py --help 输出结果为：This program prints files……

3）与arvgtest.py同一目录下，新建a.txt的记事本文件，内容为：test argv；

命令行带参数运行：arvgtest.py a.txt，输出结果为a.txt文件内容：test argv，

这里也可以多带几个参数，程序会先后输出参数文件内容





http://xpleaf.blog.51cto.com/9315560/1700811
'''