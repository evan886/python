#!/usr/bin/python
#encoding=utf-8

from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory
from twisted.protocols.basic import LineReceiver

class EchoServer(Protocol):

    def connectionMade(self): #连接建立的时候
        print 'Get connection from', self.transport.client

    def lineReceived (self, line): #将收到的数据返回给客户端
        self.transport.write(line)

factory = Factory()
factory.protocol = EchoServer

port = 1234
reactor.listenTCP(port, factory)
reactor.run() #进入循环
