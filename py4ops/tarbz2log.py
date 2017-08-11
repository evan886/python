#!/usr/bin/python
#-*- coding:utf-8 -*
# 打包并删除原来的原目录 by evan 20170810
import os, tarfile , shutil , datetime
mydate=(datetime.datetime.now() - datetime.timedelta(days=7)).strftime("%Y%m%d")
mytarfile=mydate+'.tar.bz2'

logdirs=['create','enter','levelup','login','reg','start']
os.chdir("/data/logs/yaklog/")

def mymove(src,dest):
    shutil.move(src,dest)

def make_tarbz2(tarname, srcdir):
    tar=tarfile.open(tarname, 'w:bz2') 
    tar.add(srcdir,arcname=os.path.basename(srcdir))
    tar.close()
    
#有时在centos6 上不能用 
def make_tarbz20(tarname, srcdir):
    with tarfile.open(tarname, 'w:bz2') as tar:
        tar.add(srcdir,arcname=os.path.basename(srcdir))
        tar.close()
        
if __name__=="__main__":
    
    for log in logdirs:
        mysrc="/data/logs/yaklog/"+log+'/'+mydate
        mydest="/data/logs/yaklog/"+log+'_bak'
        mymove(mysrc,mydest)

    os.chdir("/data/logs/yaklog/")
    
    for log in logdirs:
        os.chdir("/data/logs/yaklog/"+log+'_bak')
        #pass
        make_tarbz2(mytarfile,mydate)
     
        if os.path.exists(mytarfile) and os.path.exists(mydate):
            shutil.rmtree(mydate)
