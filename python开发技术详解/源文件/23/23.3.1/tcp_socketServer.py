#!/usr/bin/python
#encoding=utf-8

from SocketServer import TCPServer, StreamRequestHandler

class MyHandler(StreamRequestHandler):
	
    def handle(self): #重载处理方法
        addr = self.request.getpeername() #获取连接对端地址
        print 'Get connection from', addr
        self.wfile.write('This is a tcp socket server') #发送数据

host = ''
port = 1234
server = TCPServer((host, port), MyHandler) #生成TCP服务器

server.serve_forever() #开始监听并处理连接