#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ʹ��writelines()���ļ�
f = file("hello.txt", "w+")
li = ["hello world\n", "hello China\n"]
f.writelines(li)
f.close()    

# ׷���µ����ݵ��ļ�
f = file("hello.txt", "a+")
new_context = "goodbye"
f.write(new_context)
f.close()   
