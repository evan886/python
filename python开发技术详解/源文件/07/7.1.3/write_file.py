#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 使用writelines()读文件
f = file("hello.txt", "w+")
li = ["hello world\n", "hello China\n"]
f.writelines(li)
f.close()    

# 追加新的内容到文件
f = file("hello.txt", "a+")
new_context = "goodbye"
f.write(new_context)
f.close()   
