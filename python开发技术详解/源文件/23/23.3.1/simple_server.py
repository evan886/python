#!/usr/bin/python
#encoding=utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = socket.gethostname()
host = ""
port = 3333
s.bind((host, port))

s.listen(10)

while True:
    c, addr = s.accept()

    print 'Get connection from', addr
    c.send('This is a simple server')

    c.close()