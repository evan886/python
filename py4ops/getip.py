#!/usr/bin/python
#-*- coding:utf-8 -*-
import  socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    return  socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


print get_ip_address('eth0')

'''

send email 要用到这个ip 的东西

>>> get_ip_address('eth0')
'38.113.228.130'
http://blog.csdn.net/heizistudio/article/details/38413739

使用Python获得本机IP地址
http://www.pythonclub.org/python-network-application/get-ip-address
'''