#!/usr/bin/python
# -*- coding: UTF-8 -*-

# �����ļ�
context = '''hello world
hello China            
'''
f = file('hello.txt', 'w')   # ���ļ�
f.write(context)             # ���ַ���д���ļ�
f.close()                    # �ر��ļ�

    stdin = <open file '<stdin>', mode 'r' at 0x00B6F020>
    stdout = <open file '<stdout>', mode 'w' at 0x00B6F068>