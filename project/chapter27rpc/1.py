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
    'extracts the port from a URL'
    name = urlparse(url)[1]
    parts = name.split(':')
    return int(parts[-1])


class Node:
     """ 
     """
     def __init__(self,url,dirname,srcret):
		 self.url = url
		 self.dirname = dirname
		 self.secret = secret
		 self.know = set()
		 
		 def query(self,quer,history=[]):
			 
			 try:
				 return self._handle(query)
			except UnhandledQuery:
				history = history + [self.url]   	  

    


