import sys


def readfile(filename):
    ''' Print a file to the standard output. '''
    f = file(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line
    f.close()


# Script starts from here
if len(sys.argv) < 2:
    print ' NO action specified.'
    sys.exit()

if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    if option == 'version':
        print ' version 1.2 '
    elif option == 'help':
        print '''This program prints files to the standard output.
             Any number of files can be specified.
             Options include:
             --version : Prints the version number
             --help     : Display this help'''
    else:
        print 'Unknow option.'
else:
    for filename in sys.argv[1:]:
        readfile(filename)


'''
保存为arvgtest2.py,我们验证一下：

1）命令行带参数运行：sarvgtest2.py --version 输出结果为：version 1.2

2）命令行带参数运行：arvgtest2.py --help 输出结果为：This program prints files……

3）与arvgtest2.py同一目录下，新建a.txt的记事本文件，内容为：test argv；

命令行带参数运行：arvgtest2.py a.txt，输出结果为a.txt文件内容：test argv，

这里也可以多带几个参数，程序会先后输出参数文件内容

https://docs.python.org/2/library/sys.html
http://www.cnblogs.com/cython/articles/2196715.html
'''