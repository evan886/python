#!/usr/bin/python
#encoding=utf-8

import socket
import datetime
import sys

DEFAULT_PORT = 1235

def timeServer(port):	
	host = ''
	s = None
	for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
	    af, socktype, proto, canonname, sa = res
	    try:
	    	s = socket.socket(af, socktype, proto)
	    except socket.error, msg:
			s = None
			continue
	    try:
			s.bind(sa)
			s.listen(10)
	    except socket.error, msg:
			s.close()
			s = None
			continue
	    break
	if s is None:
	    print 'could not open socket'
	    return 1

	while True:
	    c, addr = s.accept()
	    print 'Get connection from', addr
	    c.send(str(datetime.datetime.now()))
	    c.close()

if __name__ == '__main__':
    port = DEFAULT_PORT
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
            if port<0 or port>=65536:
                port = DEFAULT_PORT
        except Exception, e:
            port = DEFAULT_PORT
    timeServer(port)