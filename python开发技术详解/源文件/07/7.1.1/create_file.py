#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 创建文件
context = '''hello world
hello China            
'''
f = file('hello.txt', 'w')   # 打开文件
f.write(context)             # 把字符串写入文件
f.close()                    # 关闭文件

    stdin = <open file '<stdin>', mode 'r' at 0x00B6F020>
    stdout = <open file '<stdout>', mode 'w' at 0x00B6F068>