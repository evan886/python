#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 使用read()、write()实现拷贝
# 创建文件hello.txt
src = file("hello.txt", "w")
li = ["hello world\n", "hello China\n"]
src.writelines(li) 
src.close()
# 把hello.txt拷贝到hello2.txt
src = file("hello.txt", "r")
dst = file("hello2.txt", "w")
dst.write(src.read())
src.close()
dst.close()


# shutil模块实现文件的拷贝
import shutil

shutil.copyfile("hello.txt","hello2.txt")
shutil.move("hello.txt","../") 
shutil.move("hello2.txt","hello3.txt") 

