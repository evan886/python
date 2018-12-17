#!/usr/bin/python
#-*- coding:utf-8 -*-
old_file_name= input(" 输入要复制的文件名 ")

old_file = open(old_file_name,"r")

#test.py  -----> test[复件].py
#new_file_name = "[复件]"+old_file_name
position = old_file_name.rfind(".")
new_file_name = old_file_name[0:position] + "[复件]" + old_file_name[position:]

new_file = open(new_file_name,"w")
#1024 == 1k
while True:
    content = old_file.read(1024)

    if len(content) ==0:
        break

    new_file.write(content)

old_file.close()
new_file.close()

