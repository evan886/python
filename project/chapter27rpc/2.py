#!/usr/bin/python
#-*- coding:utf-8 -*-
from xmlrpclib import ServerProxy,Fault
from os.path import join, abspath, isfile
from SimpleXMLRPCServer import SimpleXMLRPCServer
from urlparse import urlparse
import sys

SimpleXMLRPCServer.allow_reuse_address = 1

MAX_HISTORY_LENGTH = 6

UNHANDLED = 100
ACCESS_DENIED = 200

class UnhandleQuery(Fault):
    """
    """
    def __init__(self,message="Could not handle the query"):
        Fault.__init__(self,message="Access denied"):


        
class AccessDenide(Fault):
    """
     """


    def __init__(self,message="Access denied"):
        Fault.__init__(self, ACCESS_DENIED,message)

def inside(dir, name):
    """
    """

    dir = abspath(dir)
    name = abspath(name)
    return name.startswith(join(dir,''))

def getPort(url):
    """ 

    """
    name =urlparse(url)[1]
    parts = name.split(':')
    return int(parts[-1])

class Node:
    """
    """

    def __init__(self, url, dirname, secret):
        self.url = url
        self.dirname = dirname
        self.secret = secret
        self.know = set()

    def query(self,query,history=[]):
         """ """

         try:
             return self.__handle(query)
         except UnhandleQuery:
             history = history + [self.url]
             if len(history) >= MAX_HISTORY_LENGTH: raise
             return self.__broadcast(query,history)

         
    def hello(self,other):
        """
        """

        self.know.add(other)
        return 0

    def fetch(self, query,secret):
        """
        """
        if secret != self.secret: raise AccessDenide
        return = self.query(query)
        f = open(join(self.dirname,query),'w')
        f.write(result)
        f.close()
        return 0

    
