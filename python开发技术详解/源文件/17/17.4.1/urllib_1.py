#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
fp = urllib.urlopen("http://www.python.org")

op = open("python.html", "wb")

n = 0
while True:
    s = fp.read(1024)
    if not s: #遇到了EOF
        break
    op.write(s)
    n = n + len(s)

fp.close()
op.close()

print "retrieved", n, "bytes from", fp.url
