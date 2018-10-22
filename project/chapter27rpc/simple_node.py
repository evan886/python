#!/usr/bin/python
from xmrpclib import ServerProxy
from os.path import join, isfile
from SimpleXMLRPCServer import SimpleXMLRPCServer
from urlparse import urlparse
import sys
MAX_HISTORY_LENGTH = 6

OK = 1
FAIL = 2
EMPTY = ''


def getPort(url):
    'extracts the port from a URL 用URL中提取端口'
    name = urlparse(url)[1]
    parts = name.split(':')
    return int(parts[-1])


class Node:
     """ 
     p2p网络中的节点
     """
    def __init__(self,url,dirname,srcret):
		 self.url = url
		 self.dirname = dirname
		 self.secret = secret
		 self.know = set()
		 
    def query(self,quer,history=[]):
			 """ 
			 查询文件，可能会向其它已知节点请求帮助 将文件作为字符串返回
			 
			 """
        code, data = self._handle(query)
        if code == OK:
            return  code,data
        else:
            history = history + [self.url]
            if len(history) >= MAX_HISTORY_LENGTH:
                return FAIL, EMPTY
            return self._broadcast(query,history)
    def hello(self,other):
    
  

    


