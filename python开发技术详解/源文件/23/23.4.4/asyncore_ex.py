#!/usr/bin/python
#encoding=utf-8

import asyncore, socket

class HttpClient (asyncore.dispatcher): #定义了一个HttpClient类

    def __init__(self, host, path): #类的构造函数
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM) #创建socket对象
        self.connect( (host, 80) )
        self.buffer = 'GET %s HTTP/1.0\r\n\r\n' % path

    def handle_connect(self): #连接调用接口
        pass

    def handle_close(self): #接口关闭函数
        self.close()

    def handle_read(self): #读取数据
        print self.recv(1024)

    def handle_write(self): #写入数据
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]

    def writable(self): #判断是否写入数据
        return (len(self.buffer) > 0)

if __name__ == ‘__main__’:
c = HttpClient('www.python.org', '/')

asyncore.loop() #开始异步通信处理方式
