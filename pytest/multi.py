#!/usr/bin/env python
import multiprocessing
import time
def clock(interval):
        while True:
                print "The time is {0}".format(time.ctime())
                time.sleep(interval)
if __name__ == "__main__":
        for i in range(3):
                p = multiprocessing.Process(target=clock,args=(1,))
                p.start()
                p.join()

'''
 join()代表启动多进程，但是阻塞并发运行，一个进程执行结束后再执行第二个进程。可以给其设置一个timeout值比如join(5)代表5秒后无论当前进程是否结果都继续并发执行第二个进程

程序运行结果
The time is Mon Dec 19 17:25:14 2016
The time is Mon Dec 19 17:25:15 2016
The time is Mon Dec 19 17:25:16 2016
省略

1T= 1024G
    3999
    32768

'''