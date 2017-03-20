#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys,time

sys.stderr = open("record.log", "a")  
f = open(r"./hello.txt","r")
t = time.strftime("%Y-%m-%d %X", time.localtime())
context = f.read()
if context:
    sys.stderr.write(t + " " + context)
else:
    raise Exception, t + " “Ï≥£–≈œ¢"  


