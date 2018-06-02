#!/usr/bin/python
#*-*coding:utf8*-*
 
"""
此脚本适用于批量登录到Linux操作系统，并执行一些简单命令
要求所有服务器的用户名密码一样，或者密钥一样，都能使用同一种方法登录
执行的命令默认只输入第一行，如果要输出多行需要修改ssh_login函数
默认脚本是以用户名密码登录，也可以改为用密钥登录
选项特殊说明：
-c：后面跟要执行命令，命令如w,uptime,hostname,date等，如果命令中有空格，需要用双引号，如"cat /etc/hosts"
-a：后面跟主机，有三种写法192.168.1.31指单台主机，192.168.1.31,192.168.132,指定多台主机,把逗号换成“-”指定区间
 
如果有很多主机，但用户名密码不一样，登录方法也不一样，可以考虑把这些信息写入到一个文件，
通过对文件遍历来完成复杂环境的需求

learn$ ./login.py -a 192.168.88.3,192.168.88.2 -c "ip add  awk "
192.168.88.2	
192.168.88.3	

http://blog.51cto.com/270142877/1944923
"""
 
import paramiko
from optparse import OptionParser
import sys
import netaddr
import threading
 
#使用选项帮助信息可以使用中文
reload(sys)
sys.setdefaultencoding("utf-8")
 
#定义选项
usage = sys.argv[0] + " [选项]"
parser = OptionParser(usage)
parser.add_option('-c', '--commond',
                  dest='commond',
                  action='store',
                  default=False,
                  help='你要执行的命令，如：uptime')
parser.add_option('-a', '--host',
                  dest='host',
                  action='store',
                  default=False,
                  help='需要执行命令的主机，跟主机IP地址，多个IP用逗号分隔，也可以用“-”连接一个主机范围')
options, args = parser.parse_args()
 
def ssh_login(ip, commond):
    "登录并执行命令，可以更改为使用密钥登录"
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, port=22, username='root', password='p-0p-0p-0')
    stdin, stdout, stderr = ssh.exec_command(commond)
    print('%s\t%s' %(ip, stdout.readline().rstrip()))
    ssh.close()
 
if __name__ == '__main__':
    if not options.commond:
        print("请指定要执行的命令")
        exit(1)
    if not options.host:
        print("请指定主机")
        exit(1)
 
    if ',' in options.host:
        ip = options.host.split(',')
        for i in ip:
            t = threading.Thread(target=ssh_login, args=(i, options.commond))   #使用线程方式执行，更快
            t.start()
    elif '-' in options.host:
        startip = options.host.split('-')[0]
        endip = options.host.split('-')[1]
        ip = list(netaddr.IPRange(startip, endip))        #netaddr.IPRange()用于计算IP地址区间内的所有IP
        for i in ip:
            t = threading.Thread(target=ssh_login, args=(str(i), options.commond))
            t.start()
    else:
        ip = options.host
        ssh_login(ip, options.commond)
