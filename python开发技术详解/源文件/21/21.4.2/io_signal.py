#!/usr/bin/python
#encoding=utf-8

import signal

def sigint_handler(signum, frame): #SIGINT信号处理函数
    print “In signal SIGINT handler”
signal.signal( signal.SIGINT, sigint_handler) #注册SIGINT信号处理函数

while True:
ret = raw_input(‘Prompt>’> #I/O处理，将在这里发生中断
print “Hello, “, ret


