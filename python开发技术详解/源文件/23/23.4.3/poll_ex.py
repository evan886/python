#!/usr/bin/python
#encoding=utf-8

import socket, select #生成socket对象

s = socket.socket() #

host = socket.gethostname()
port = 1234
s.bind((host, port)) #绑定套接字接口地址

fd_dict = {s.fileno(): s}

s.listen(5) #开始服务器端监听

p = select.poll() #生成Polling对象
p.register(s) #注册socket对象

while True:
events = p.poll() #获取准备好的文件对象

    for fd, event in events:
        if fd in fd_dict:
            c, addr = s.accept() #处理连接
            print 'Got connection from', addr
            p.register(c)
            fd_dict[c.fileno()] = c #加入连接socket

        elif event & select.POLLIN:
            data = fd_dict[fd].recv(1024) #接收时间
            if not data: 
                print fd_dict[fd].getpeername(), 'disconnected'
                p.unregister(fd) #取消注册
                del fd_dict[fd]
            else:
                print data #打印数据