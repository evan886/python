#!/usr/bin/python
#encoding=utf-8

import subprocess

pingP=subprocess.Popen(args=’ping –n 4 www.sina.com.cn’, shell=True) #生成ping进程
pingP.wait() #等待进程完成
pirnt pingP.pid #打印进程ID
print pingP.returncode #打印进程返回值
