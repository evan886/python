#-*- coding:utf-8 -*-
file_name = input('输入打开的文件名:')
f = open(file_name)
print('文件的内容是:')
for each_line in f:
    print(each_line)
