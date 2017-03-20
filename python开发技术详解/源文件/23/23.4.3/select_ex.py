#!/usr/bin/python
#encoding=utf-8

import socket, select

s = socket.socket() #生成socket对象

host = socket.gethostname()
port = 1234
s.bind((host, port)) #绑定套接字接口地址

s.listen(5) #开始服务器端监听

inputs = [s]
while True:
    rs, ws, es = select.select(inputs, [], []) #使用select方法
    for r in rs:
        if r is s:
            c, addr = s.accept() #处理连接
            print 'Get connection from', addr
            inputs.append(c)
        else:
            try:
                data = r.recv(1024) #接收数据
                disconnected = not data
            except socket.error:
                disconnected = True

            if disconnected:
                print r.getpeername(), 'disconnected'
                inputs.remove(r)
            else:
                print data #打印接收到的数据

