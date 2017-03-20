#!/usr/bin/python
#encoding=utf-8

from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory
from twisted.protocols.basic import LineReceiver

class SimpleServer(Protocol):

    def connectionMade(self): #连接建立的时候
        print 'Get connection from', self.transport.client
        
    def connectionLost(self, reason):连接断开的时候
        print self.transport.client, 'disconnected'
        
    def lineReceived(self, line): #当收到一行数据的时候
        print line        

factory = Factory()
factory.protocol = SimpleServer

port = 1234
reactor.listenTCP(port, factory)
reactor.run() #进入循环

