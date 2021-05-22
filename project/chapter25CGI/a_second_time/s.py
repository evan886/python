# -*- coding: utf-8 -*-
import os
from http.server import HTTPServer, CGIHTTPRequestHandler
webdir = "./"
port = 80
os.chdir(webdir)
srvraddr = ("localhost", port)
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()
