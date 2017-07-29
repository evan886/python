#-*- coding: utf-8 -*-
import time 

# 定义一个计时器，传入一个，并返回另一个附加了计时功能的方法
def timeit(func):

    # 定义一个内嵌的包装函数，给传入的函数加上计时功能的包装
    def wrapper():
        start = time.clock()
        print 'start time:' 
        print start 
        func()
        end = time.clock()
        print 'end time'
        print end 
        print 'used:', end - start

    # 将包装后的函数返回
    return wrapper

print @timeit
def foo():
    print 'in foo()'

 
