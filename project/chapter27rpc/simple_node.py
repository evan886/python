#!/usr/bin/python
#-*- coding:utf-8 -*-
from xmlrpclib import ServerProxy
from os.path import join, isfile
from SimpleXMLRPCServer import SimpleXMLRPCServer
from urlparse import urlparse
import sys
MAX_HISTORY_LENGTH = 6

OK = 1
FAIL = 2
EMPTY = ''

def

def getPort(url):
    'extracts the port from a URL 用URL中提取端口'
    name = urlparse(url)[1]
    parts = name.split(':')
    return int(parts[-1])

class Node:
     """ 
     p2p网络中的节点
     """
     def __init__(self,url,dirname,secret):
         self.url = url
         self.dirname = dirname
         self.secret = secret
         self.known = set()
     def query(self,quer,history=[]):
         """
             查询文件，可能会向其它已知节点请求帮助 将文件作为字符串返回
         """
         code, data = self._handle(query)
         if code == OK:
             return code, data
         else:
             history = history + [self.url]
             if len(history) >= MAX_HISTORY_LENGTH:
                 return FAIL, EMPTY
             return self._broadcast(query,history)
     def  hello(self,other):
          """
          """
          self.know.add(other)
          return OK
     def fetch(self, query,secret):
         """
         """
         if secret != self.secret: return FAIL
         code, data = self.query(query)
         if code == OK:
             f = open(join(self.dirname,query),'w')
             f.write(data)
             f.close()
             return OK
         else:
             return FAIL

     def _start(self):
         """
         """
         s = SimpleXMLRPCServer(("",getPort(self.url)),logRequests=False)
         s.register_instance(self)
         s.serve_forever()
        
     def _handle(self, query):
         """
         """
         dir = self.dirname
         mane = join(dir,query)

     def _broadcast(self,query, history):
         """
         here20181026
         """
         for other in self.known.copy():
             if other in history: continue
             try:
                 s = ServerProxy(other)
                 code, data = s.query(query,history)
                 if code == OK:
                     return code,data
             except:
                 self.known.remove(other)
         return FAIL, EMPTY
def main():
    url,directory, secret = sys.argv[1:]
    n = Node(url,directory,secret)
    n._start()


if __name__ == "__main__":
    main()

'''
python simple_node.py  http://localhost:4242 files1 secret1

python simple_node.py  http://localhost:4243 files2 secret2


In [1]: from xmlrpclib import *

In [2]: mypeer = ServerProxy('http://localhost:4242')

In [3]: code , date = mypeer.query('test.txt')


Fault: <Fault 1: "<type 'exceptions.NameError'>:global name 'query' is not defined">





'''
