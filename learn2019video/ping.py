#--*-- coding:utf-8 --*--
from __future__ import print_function
#import pdb
import subprocess
import threading
# ping -c 1 ip_address 
def is_reacheable(ip):
    if subprocess.call(["ping","-c","1",ip]):
        print("{0} is  unreacheable".format(ip))
    else:
        print("{0} is alive".format(ip))

'''
subprocess.call 成功是返回0,而python中 0 是不成功
def is_reacheable(ip):
    if subprocess.call(["ping","-c","1",ip]):
        print("{0} is alive".format(ip))
    else:
        print("{0} is unreacheable".format(ip))
'''

def main():
    with open('ips.txt') as f:
        lines = f.readlines()
        threads = []
        for line in lines:
            thr = threading.Thread(target=is_reacheable,args=(line,))
            thr.start()
            threads.append(thr)

        for thr in threads:
            thr.join() #阻塞直到队列中的所有项目全被 删除和处理为止

if __name__ == '__main__':
    main()
