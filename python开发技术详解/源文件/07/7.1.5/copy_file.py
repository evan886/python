#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ʹ��read()��write()ʵ�ֿ���
# �����ļ�hello.txt
src = file("hello.txt", "w")
li = ["hello world\n", "hello China\n"]
src.writelines(li) 
src.close()
# ��hello.txt������hello2.txt
src = file("hello.txt", "r")
dst = file("hello2.txt", "w")
dst.write(src.read())
src.close()
dst.close()


# shutilģ��ʵ���ļ��Ŀ���
import shutil

shutil.copyfile("hello.txt","hello2.txt")
shutil.move("hello.txt","../") 
shutil.move("hello2.txt","hello3.txt") 

