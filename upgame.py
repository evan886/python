#!/usr/bin/env python
# -*- coding: utf-8 -*-
## author  www.linuxchina.net     Merge in 2016-05-17   tmld game update files 
## 备份
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
#pass func
#把某一目录下的所有文件复制到指定目录中  也会 覆盖文件内容呀   coverFiles 感觉可以不要了 
def copyFiles(sourceDir,  targetDir):  
     if sourceDir.find(".svn") > 0: 
         return 
     for file in os.listdir(sourceDir): 
         sourceFile = os.path.join(sourceDir,  file) 
         targetFile = os.path.join(targetDir,  file) 
         if os.path.isfile(sourceFile): 
             if not os.path.exists(targetDir): 
                 os.makedirs(targetDir) 
             #if not os.path.exists(targetFile) or(os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))): 
             open(targetFile, "wb").write(open(sourceFile, "rb").read()) 
         if os.path.isdir(sourceFile): 
             First_Directory = False 
             copyFiles(sourceFile, targetFile)        
#copyFiles(localpath+'/tempdll/',installpath+'/DBServer/x64')

#split("_")[-1]) 是防止其它不规范的split而已 ，不一定有_
def get_spid():
    spid = []
    zones = []
    if games:
        #spid = games[0].split("_")[1]   ; games -->  ['D:/games\\t5', 'D:/games\\t6']
        VSPDef = r"%s\data\VSPDef.txt" % games[0]
        with open(VSPDef,"r") as f:
            for line in f.readlines():
                if "SPID =" in line:
                    spid = line.split("=")[-1].strip()
        for zone in games:
            print zone
            zones.append(zone.split("\\")[-1].split("_")[-1])
    else:
        print u"空服务器"
        exit(1)
    return spid,zones

nowdata = time.strftime('%Y-%m-%d')

upbakdir = r'D:\upbakdir'

localpath = r'D:\update'
localupdir =  r'D:\update'

nowdata = time.strftime('%Y-%m-%d')
#nowdata ='2016-05-19'

savepath = localpath+'/'+nowdata
games_path = 'D:/games'


'''
files = os.listdir.('xxx')
for each in firlse:
    zipfile_func(each)
'''


        
#new 20160513  r up patch 
#作用 解压 patch 目录下的所有文件在一起    不能覆盖，会出 错,关于这个问题 应该是在整个脚本执行完后删除 patch目录下的所有东西     一开始报错是 win 目录写法问题，全用 / unix写法就好了 
#def myunzip4patch(zfiles,path):
def myunzip4patch(zfiles):
    #print localpath+'/'+nowdata+'/patch/'+zfiles
    zfile=zipfile.ZipFile(localpath+'/'+nowdata+'/patch/'+zfiles,'r')
    #zfile=zipfile.ZipFile(r"D:/update/2016-05-17/patch/" +zfiles,'r')
    #zfile=zipfile.ZipFile(savepath+'/LogicServer.zip','r')
    for  filename in zfile.namelist():
        zfile.extract(filename,localpath+'/'+nowdata+'/patch/')
        #zfile.extract(filename,'D:/update/2016-05-17/patch')
        #data = zfile.read(filename)
        #zf = open(deploypath+'/x64/'+filename, 'w+b')
        #zf.write(data)
        #zf.close()
    zfile.close()

#def myunzip4logic(zfiles,path):  这些如果 src tar 可以提取出来就好了  here
def myunzip4logic(zfiles):
    zfile=zipfile.ZipFile(localpath+'/'+nowdata+'/' +zfiles,'r')
    for  filename in zfile.namelist():
        zfile.extract(filename,localpath+'/'+nowdata+'/x64/')
        #zfile.extract(filename,installpath+'/x64/')
        #data = zfile.read(filename)
        #zf = open(deploypath+'/x64/'+filename, 'w+b')
        #zf.write(data)
        #zf.close()
    zfile.close()
 
#files = os.listdir('D:/update/2016-05-13/patch')  
#for each in files:
#   myunzip4logic(each)  
    #print each

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

'''
会自己覆盖     作用:覆盖文件    好像用不上在这里 
'''
def coverFiles(sourceDir,  targetDir): 
        for file in os.listdir(sourceDir): 
            sourceFile = os.path.join(sourceDir,  file) 
            targetFile = os.path.join(targetDir,  file) 
            #cover the files 
            if os.path.isfile(sourceFile): 
                open(targetFile, "wb").write(open(sourceFile, "rb").read())
                
mysrc = 'D:/update'
mytar = 'D:/games/t5'

if __name__=="__main__":
    
    games_path = 'D:/games'
    games = glob.glob(r"%s/[c|t|s][0-9]*" % games_path)
    
    # 获取spid  yy  ['t5','t6']
    spid,zones = get_spid()
    #print spid,zones
    
    #1.备份logic 直接利用 cpfunc就好了  只是后面这个命令而 tx+time 
    #这个可以用变量的 
    #gamesupdate_path = 'D:/update/2016-05-18/patch' #here var 统一一下
    gamesupdate_path = localupdir+'/'+nowdata+'/patch'
    upfiles = glob.glob(r"%s/" % gamesupdate_path)
    #print upfiles #['D:/update/2016-05-13/patch/']
    
    #解压patch   rmdir  os.removedirs（r“c：\python”） #localupdir
    files = os.listdir(localupdir+'/'+nowdata+'/patch/')
    #files = os.listdir(localpath+'/'+nowdata+'/patch/')
    #upbakfiles=os.listdir(path); 
    #files = os.listdir('D:/update/2016-05-17/patch') #很多时间不能写"" 目录时不要少了 '/'
    #print files
    
    #logicfiles = os.listdir('D:/update/2016-05-13/LogicServer.zip')
    #shutil.rmtree('D:/update/2016-05-13/patch/data/');
    #解压和cp 4 patch   
    for each in files:
        myunzip4patch(each)  
        #print each
    #myunzip4logic();

    #for eachlog in logicfiles:
        #myunzip4patch(eachlog)  
        #print eachlog
    myunzip4logic('LogicServer.zip');   
    
    for zone in zones:
        #这里的t5 t6 要用变量替换 还有要怎么拿出这里个问题      
        #cp files 4 patch and logic   gamesupdate_path = localupdir+nowdata+'/patch'
        #print localupdir+nowdata+'/patch'+'/data/'
        copyFiles(localupdir+'/'+nowdata+'/patch'+'/data/',games_path+'/'+zone+'/data/')
        #copyFiles(gamesupdate_path+'/data/',games_path+'/'+zone+'/data/')
        #copyFiles(gamesupdate_path+'/data/',games_path+'/t5/data/')
        #copyFiles(savepath+'/x64/', games_path+'/'+zone+'/x64/') #here mark 
        #copyFiles(savepath+'/x64/', games_path+'/t5/x64/')
    
        #pre_upbak 先create dir  创建单个目录：os.mkdir（“test”）  os.mkdir('t5'+nowdata) 提取出t5 为变量    用那个get_spid 吧 
        #创建多级目录：os.makedirs（r“c：\python\test”）
        os.makedirs(upbakdir+'/'+zone+nowdata)
        #copyFiles(games_path+'/'+zone+'/x64/', upbakdir+'/'+zone+nowdata)
        #logic bak 单个文件的cp   2016-0518
        shutil.copy(games_path+'/'+zone+'/x64/LogicServerCQ64_R.exe',upbakdir+'/'+zone+nowdata)
        shutil.copy(games_path+'/'+zone+'/x64/LogicServerCQ64_R.map',upbakdir+'/'+zone+nowdata)
        shutil.copy(games_path+'/'+zone+'/x64/LogicServerCQ64_R.pdb',upbakdir+'/'+zone+nowdata)
        
         
        #copyFiles(games_path+'/t5/x64/', upbakdir+'/'+'t5'+nowdata)
        
    

    
    
    
    
       
    #应该是在整个脚本执行完后删除 patch目录下的所有东西 
    #os.removedirs('D:/update/2016-05-13/patch/data')
    
    '''
    games_path = 'D:/games'
    games = glob.glob(r"%s/[c|t|s][0-9]*" % games_path)
    print games  #['D:/games\\t5', 'D:/games\\t6']
    
          列表遍历
for element in sample_list:
    print(element)
    '''
    #zones = get_spid()
    #print zones

    #for tno in zones:
    #   print tno
    #    copyFiles(sourceDir, targetDir) #here
    
    
    '''
    #here 
    #coverFiles(mysrc, mytar)
    #glob 可以列出 update 目录下的其它目录 
    #先解压 start here  先判断有没有更新 
    nowsrc=mysrc+'/'+nowdata
    #if os.path.isdir()
    if os.path.exists(nowsrc) == True:
        print "有更新 准备更新动作"
        #os._exit(0)
    else:
        print "没有更新文件，脚本停止"
        os._exit(0)
        
    # 更新分成几个来 第一个是patch  希望path里面的能写死，不能的话就只能list出来了
    nowpath=mysrc+'/'+nowdata+'/patch' 
    if os.path.exists(nowpath) == True:
        print "准备更新path"
            
    myunzip4logic()
        
#    if os.path.exists(path)
    
    #os.walk
#    copyFiles(mysrc, mytar)




'''

'''
0. 更新之前作判断  有这个文件才动手
1.备份  用    list for 备份logic就可以了    但是如果没得选择备份就很大，就像选择又在rename 也是麻烦 所以建议能在测试服中先更新，测试没事再全服更新
2.logic patch 分别用各自的func  看能不能重用一下
3. 服的选择可以用那个   VSPDef.txt  func get_spid

4.ftp自己的可以用晓同学的那个py 然后本地有个目录先同步到一台服务器上 ，然后其它服务器在这台服务器拉过去 

如果有这个目录 
就cp 过去  

最后是删除    

gs=1
if    data  unzip 

copyFiles( data  t1/data) 
fi    
'''
    
'''
Python程序退出方式(sys.exit() os._exit() os.kill() os.popen(...))
http://www.cnblogs.com/be-saber/p/4771176.html


'''    
