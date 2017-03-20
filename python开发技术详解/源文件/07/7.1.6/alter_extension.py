#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 修改后缀名
import os  
files = os.listdir(".")
for filename in files:
    pos = filename.find(".")
    if filename[pos + 1:] == "html":
        newname = filename[:pos + 1] + "htm"
        os.rename(filename,newname)

# 修改后缀名2
import os  
files = os.listdir(".")
for filename in files:
    li = os.path.splitext(filename) 
    if li[1] == ".html":
        newname = li[0] + ".htm"
        os.rename(filename,newname)