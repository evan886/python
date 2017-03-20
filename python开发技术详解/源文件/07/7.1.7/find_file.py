#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
# 文件的查找
f1 = file("hello.txt", "r")
count = 0
for s in f1.readlines():    
    li = re.findall("hello", s)
    if len(li) > 0:
        count = count + li.count("hello")
print "查找到" + str(count) + "个hello"
f1.close()

# 文件的替换
f1 = file("hello.txt", "r")
f2 = file("hello3.txt", "w")
for s in f1.readlines():    
    f2.write(s.replace("hello", "hi"))
f1.close()
f2.close()
 
