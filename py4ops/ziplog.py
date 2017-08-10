#/usr/bin/python
#-*- coding:utf-8 -*-
# 作用 压缩所有的相关目录下的log文 为服务器节省空间  https://docs.python.org/2/tutorial/interpreter.html#source-code-encoding

import os ,sys,subprocess,commands
import os.path
import shutil
import zipfile
#import zfile
import urllib
import re
from datapy import localpath
import time,  datetime
import glob

mysrc = 'D:/update'
mytar = 'D:/games/t5'

#/data/logs/yaklog
#create  enter  error.log  levelup  login  pay  reg  start
#/data/logs/yaklog/create/20170807/create_1238.log


#1 获取某指定目录下的所有子目录的列表
def getDirList( p ):
        p = str( p )
        if p=="":
              return [ ]
        p = p.replace( "/","\\")
        if p[ -1] != "\\":
             p = p+"\\"
        a = os.listdir( p )
        b = [ x   for x in a if os.path.isdir( p + x ) ]
        return b
#print   getDirList( "D:\\update" )
#['2016-04-22', '2016-05-09', 'tempconf', 'tempdll']

nowdata=time.strftime('%Y%m%d')

upbakdir = r'D:\upbakdir'
localpath = r'D:\update'


savepath = localpath + '/' + nowdata
games_path = 'D:/games'

'''
files = os.listdir.('xxx')
for each in firlse:
    zipfile_func(each)
'''

# new 20160513  r up patch
# 作用 解压 patch 目录下的所有文件在一起    不能覆盖，会出 错,关于这个问题 应该是在整个脚本执行完后删除 patch目录下的所有东西     一开始报错是 win 目录写法问题，全用 / unix写法就好了
# def myunzip4patch(zfiles,path):
def myunzip4patch(zfiles):
    # print localpath+'/'+nowdata+'/patch/'+zfiles
    zfile = zipfile.ZipFile(localpath + '/' + nowdata + '/patch/' + zfiles, 'r')
    # zfile=zipfile.ZipFile(r"D:/update/2016-05-17/patch/" +zfiles,'r')
    # zfile=zipfile.ZipFile(savepath+'/LogicServer.zip','r')
    for filename in zfile.namelist():
        zfile.extract(filename, localpath + '/' + nowdata + '/patch/')
        # zfile.extract(filename,'D:/update/2016-05-17/patch')
        # data = zfile.read(filename)
        # zf = open(deploypath+'/x64/'+filename, 'w+b')
        # zf.write(data)
        # zf.close()
    zfile.close()


if __name__ == "__main__":
    games_path = 'D:/games'
    games = glob.glob(r"%s/[c|t|s][0-9]*" % games_path)


#zipfile.is_zipfile(filename)：判断一个文件是不是压缩文件

# https://docs.python.org/2/library/zipfile.html#zipfile-objects
import glob



if not zipfile.is_zipfile(filename):
    zip



files=glob.glob('/data/logs/yaklog/create/20170807/')
for file in files:

    pass

f.close

import zipfile
myzip=zipfile.ZipFile('a.zip','w')
myzip_write('afile',compre)

with ZipFile('spam.zip', 'w') as myzip:
    myzip.write('eggs.txt')



创建一个新的ZIP文件


from zipfile_infolist import print_info
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
print_info('zipfile_write.zip')


"""
If you want to create a new ZIP archive, specify its name after the -c option and then list the filename(s) that should be included:
$ python -m zipfile -c monty.zip spam.txt eggs.txt

Passing a directory is also acceptable:
$ python -m zipfile -c monty.zip life-of-brian_1979/

for 





# split("_")[-1]) 是防止其它不规范的split而已 ，不一定有_
def get_spid():
    spid = []
    zones = []
    if games:
        # spid = games[0].split("_")[1]   ; games -->  ['D:/games\\t5', 'D:/games\\t6']
        VSPDef = r"%s\data\VSPDef.txt" % games[0]
        with open(VSPDef, "r") as f:
            for line in f.readlines():
                if "SPID =" in line:
                    spid = line.split("=")[-1].strip()
        for zone in games:
            print zone
            zones.append(zone.split("\\")[-1].split("_")[-1])
    else:
        print u"空服务器"
        exit(1)
    return spid, zones
"""


