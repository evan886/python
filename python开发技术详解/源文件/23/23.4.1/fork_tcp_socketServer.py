#!/usr/bin/python
#encoding=utf-8

from SocketServer import TCPServer, ForkingMixIn, StreamRequestHandler
import time

class Server(ForkingMixIn, TCPServer): #自定义Server类
	pass

class MyHandler(StreamRequestHandler):
	
    def handle(self): #重载handle函数
        addr = self.request.getpeername()
        print 'Get connection from', addr #打印客户端地址
        time.sleep(5) #休眠5秒钟
        self.wfile.write('This is a ForkingMixIn tcp socket server') #发送信息

host = ''
port = 1234
server = Server((host, port), MyHandler)

server.serve_forever() #开始侦听并处理连接
