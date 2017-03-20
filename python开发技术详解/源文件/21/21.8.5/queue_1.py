#!/usr/bin/python
#encoding=utf-8

import threading, Queue
import time, random

class Worker(threading.Thread): #工作类
    def __init__(self, index, queue): #构造函数
        threading.Thread.__init__(self)
        self.index = index
        self.queue = queue
    def run(self):
        while 1: 
            time.sleep(random.random())
            item = self.queue.get() #从同步队列中获取对象
            if item is None: #循环终止条件
                break
            print "index:",self.index, "task", item, "finished"
            self.queue.task_done() 

queue = Queue.Queue(0) #生成一个不限制长度的同步队列
for i in range(2):
    Worker(i, queue).start() #生成两个线程
for i in range(10):
    queue.put(i) #向同步队列中加入对象
for i in range(2):
    queue.put(None)
