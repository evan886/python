# -*- coding:utf-8 -*-
##############################################################
#   rPyc模块的调用
#   目的是为了A执行机上，能在B机上执行cmd命令并且获取返回值
#   rPyc 服务端
##############################################################

from rpyc import Service
from rpyc.utils.server import ThreadedServer
import os, subprocess

class Test_ThreadedServer(Service):
    #对服务端来说，只有以“exposed_*开头的方式才能被客户端调用，所以要提供给客户端的方法都得加"exposed_”

    #返回0和1； 0=True，1=False
    def exposed_execCmd(self,cmd):
        return os.system(cmd)

    #返回cmd命令的查询结果
    def exposed_execGetCmdRsp(self,cmd):
        return os.popen(cmd).read()

    # 返回0和1； 0=True，1=False
    def exposed_subprocessCmd(self,cmd):
        return subprocess.call(cmd)

    # 返回cmd命令的查询结果
    def exposed_subprocessCmdRsp(self, cmd):
        return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()

Test_server = ThreadedServer(Test_ThreadedServer, port=6677, auto_register=False)
Test_server.start()
