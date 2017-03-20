#!/usr/bin/python
#encoding=utf-8

import thread
import time

def worker(index,create_time): #具体的线程
print (time.time()-create_time),"\t\t",index
print "Thread %d exit..." % (index)

for index in range(5):    
thread.start_new_thread(worker, (index,time.time())) #启动线程

print "Main thread exit...
