#!/usr/bin/python
#encoding=utf-8

from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory
from twisted.protocols.basic import LineReceiver

class EchoServer(Protocol):

def connectionMade(self): #连接建立的时候
        print 'Get connection from', self.transport.client
        self.factory.numProtocols = self.factory.numProtocols+1
        if self.factory.numProtocols > 5: #当连接超过5个的时候，断开连接
            self.transport.write("Too many connections, try later")
            self.transport.loseConnection()
        print 'Get connection from', self.transport.client

    def connectionLost(self, reason): #断开连接
        self.factory.numProtocols = self.factory.numProtocols-1

    def lineReceived (self, line): #将收到的数据返回给客户端
        self.transport.write(line)

factory = Factory()
factory.protocol = EchoServer

port = 1234
reactor.listenTCP(port, factory)
reactor.run() #进入循环

