#!/usr/bin/python
#-*- coding:utf-8 -*-
from multiprocessing import  Process, Queue

def f(q):
    q.put([1,2,3,4])

if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q=Queue()
    p=Process(target=f,args=(q,))
    p.start()
    ### 读数据进程执行的代码:
    print q.get()
    p.join()

'''
#运行结果
[1, 2, 3, 4]
'''