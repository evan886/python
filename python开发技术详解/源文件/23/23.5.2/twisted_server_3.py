#!/usr/bin/python
#encoding=utf-8

from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory

class SimpleServer(Protocol):

    def connectionMade(self): #连接建立的时候
        print 'Get connection from', self.transport.client
self.transport.loseConnection()

factory = Factory()
factory.protocol = SimpleServer

port = 1234
reactor.listenTCP(port, factory)
reactor.run() #进入循环


