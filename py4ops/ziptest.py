#!/usr/bin/python
#-*- coding:utf-8 -*-

#创建一个新的ZIP文件



#from zipfile import print_info
import zipfile


print 'creating archive'
zf = zipfile.ZipFile('zipfile_write.zip', 'w')
try:
    print 'adding text.txt'
    zf.write('a.txt')
finally:
    print 'closing'
    zf.close()

print

#print_info('zipfile_write.zip')

"""

"""