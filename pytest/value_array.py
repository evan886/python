#!/usr/bin/python
#-*- coding:utf-8 -*-
from multiprocessing import  Process, Value,Array
def f(n,a):
    n.value=3.1415926
    for i in range(len(a)):
        a[i]=-a[i]
if __name__ == "__main__":
    num =Value('d',0.0)
    arr = Array('i',range(10))
    p=Process(target=f,args=(num,arr))
    p.start()
    p.join()
    print num.value
    print arr[:]


'''
join()代表启动多进程
启动子进程p p.start()

运行结果

3.1415926
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

'''


