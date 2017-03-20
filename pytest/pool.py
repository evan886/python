#!/usr/bin/python
#-*- coding: utf-8 -*-
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'

'''
运行结果
evan@evanpc:~/dkm/python/test$ python pool.py
Parent process 23349.
Waiting for all subprocesses done...
Run task 0 (23350)...
Run task 1 (23351)...
Run task 2 (23352)...
Run task 3 (23353)...
Task 3 runs 1.04 seconds.
Run task 4 (23353)...
Task 4 runs 0.05 seconds.
Task 2 runs 1.37 seconds.
Task 0 runs 1.80 seconds.
Task 1 runs 2.92 seconds.
All subprocesses done.

'''
