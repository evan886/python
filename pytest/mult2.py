#!/usr/bin/python
#-*-  coding:utf-8 -*-

from multiprocessing import Process, Lock
def f(l,i):
    l.acquire()
    print "hellow world", i
    l.release()

if __name__ == "__main__":
    lock = Lock()
    for num in range(10):
        Process(target=f, args=(lock,num)).start()


'''
二:进程同步
    对于一些互斥的资源来说，进程间需要进程互斥来访问。否则导致资源访问受阻，或者最后的结果混乱等情况。对于标准输出这个资源来说，如果多个资源同属输出信息，可能会导致输出的信息混乱。所以需要使用锁来避免资源互斥访问。

程序运行结果
hellow world 0
hellow world 5
hellow world 1
hellow world 4
hellow world 3
hellow world 9
hellow world 7
hellow world 8
hellow world 6
hellow world 2

mysqlimport [options] db_name textfile1 [textfile2 …]

/:parameter

'''