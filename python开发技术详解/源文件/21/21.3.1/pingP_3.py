#!/usr/bin/python
#encoding=utf-8

import subprocess

pingP=subprocess.Popen(args=’ping –n 4 www.sina.com.cn’, shell=True, stdout = subprocess.PIPE)
pingP.wait() #等待进程完成
print pingP.stdout.read() #读取进程的输出信息
print pingP.pid
print pingP.returncode
