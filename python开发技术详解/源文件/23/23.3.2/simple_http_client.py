#!/usr/bin/python
#encoding=utf-8

import socket
import urlparse
import sys

def httpget(url):
	up = urlparse.urlparse(url) #解析URL
	host = up[1]
	page = up[2]
	s = socket.socket() #生成socket对象

	port = 80 #使用80端口号
	s.connect((host, port)) 连接服务器

	cmd = "get "+ page+"\n"
	s.send(cmd) #发送HTTP命令

	print s.recv(1024) #获取内容

	s.close() #关闭连接

if __name__ == "__main__":
	httpget(sys.argv[1]) #调用httpget函数