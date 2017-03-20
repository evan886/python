#!/usr/bin/python
#encoding=utf-8

import threading
import time

class Counter: #计数器类
    def __init__(self):
        self.value = 0
    def increment(self):
        self.value = self.value + 1 #将value值加1
        value = self.value #并返回这个value值
        return value

counter = Counter()

class ThreadDemo(threading.Thread):
#省略了__init__构造函数
    def run(self):
        time.sleep(1)
value = counter.increment()
        print (time.time()-self.create_time),"\t",self.index, “\tvalue: ”, value

for index in range(100): #将生成100个线程
    thread = ThreadDemo (index, time.time())
    thread.start() #启动线程
