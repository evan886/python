#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
# �ļ��Ĳ���
f1 = file("hello.txt", "r")
count = 0
for s in f1.readlines():    
    li = re.findall("hello", s)
    if len(li) > 0:
        count = count + li.count("hello")
print "���ҵ�" + str(count) + "��hello"
f1.close()

# �ļ����滻
f1 = file("hello.txt", "r")
f2 = file("hello3.txt", "w")
for s in f1.readlines():    
    f2.write(s.replace("hello", "hi"))
f1.close()
f2.close()
 
