#!/usr/bin/python
#-*-  coding:utf-8 -*-

from multiprocessing import  Pool
def f(x):
    return x*x
if __name__ == '__main__':
    pool = Pool(processes=5)
    result = pool.apply_async(f,[10])
    print result
    print result.get(timeout=1)
    print pool.map(f,range(10))



'''
解说

pool常用的函数有:
apply 开启多个进程并发执行
apply_async 同上，但是这个是异步的，非阻塞的。
map 类似于内建函数map，后面提供的参数列表会一个一个应用于函数,。这里会开发多个进程并发一起执行。
map_async 和map相同，只不过这是一个异步的，不会阻塞等待结果。该函数会返回一个结果对象。


运行结果
<multiprocessing.pool.ApplyResult object at 0x7f548909ce10>
100
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
'''

'''
把当前目录下面的file（不包括目录)，移动到/opt/shell


find  .  -type f  -exec mv {}   /opt/shell   \;

find .  -type f  |  xargs  -I  '{}'  mv  {}  /opt/shell

30天的的文件 mv走
find ./ -type f -mtime +29 -exec mv {}   /data1/bak   \


http://blog.csdn.net/hardwin/article/details/7711635
'''