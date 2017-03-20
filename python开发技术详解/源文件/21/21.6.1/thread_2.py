#!/usr/bin/python
#encoding=utf-8

import thread
import time

def worker(index,create_time):
    time.sleep(1) #休眠1秒钟
print (time.time()-create_time),"\t\t",index
print "Thread %d exit..." % (index)

for index in range(5):    
thread.start_new_thread(worker, (index,time.time())) #启动5个线程

print "Main thread exit..."
