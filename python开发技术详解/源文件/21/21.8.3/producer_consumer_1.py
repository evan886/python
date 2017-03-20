#!/usr/bin/python
#encoding=utf-8

from threading import Thread, Condition, currentThread
import time

class Goods: #产品类
    def __init__(self): #初始化函数
        self.count=0
    def produce(self,num=1): #产品增长
        self.count += num
    def consume(self): #产品减少
        if self.count:
            self.count -= 1
    def isEmpty(self): #判断产品是否为空
        return not self.count

class Producer(Thread): #生产者类
    def __init__(self,condition,goods,sleeptime=1):
        Thread.__init__(self)
        self.cond=condition
        self.goods=goods
        self.sleeptime=sleeptime

    def run(self):
        cond=self.cond
        goods=self.goods
        while 1 : 
            cond.acquire() 
            goods.produce()
            print "Goods Count: ", goods.count, "Producer thread produced "
            cond.notifyAll() #通知满足此条件变量的线程
            cond.release()
            time.sleep(self.sleeptime)

class Consumer(Thread): #消费者类
    def __init__(self,index, condition,goods,sleeptime=4):
        Thread.__init__(self, name = str(index))
        self.cond=condition
        self.goods=goods
        self.sleeptime=sleeptime
    def run(self):
        cond=self.cond
        goods=self.goods
        while 1:
            time.sleep(self.sleeptime)
            cond.acquire() 
            while goods.isEmpty():
                cond.wait() #如果为空，则等待
            goods.consume()
            print "Goods Count: ", goods.count, "Consumer thread",currentThread().getName(),"consumed "
            cond.release() 
        
goods=Goods()
cond=Condition()

producer=Producer(cond,goods)
producer.start() #启动生产者线程
producer.join() #等待生产者线程完成
for i in range(5):
    consumer = Consumer(i,cond,goods)
    consumer.start() #启动5个消费者线程
    consumer.join()
