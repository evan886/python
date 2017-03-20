#!/usr/bin/python
# -*- coding: utf8 -*-
# Author :evan886@gmail.com

import requests
import os
import time
from datetime import datetime, timedelta


def opsrestart():
    try:
        urls=['http://127.0.0.1/check.php', 'http://127.0.0.1/check.html']
        while True:
            sleep = 10
            for url in urls:
                print ('get %s' %url)
                r= requests.get(url,timeout=10)
                if r.status_code == 200:
                    print ('%s is ok ' % url)
                    print ('moniter continue after 10s')
            time.sleep(sleep)
    except Exception as e:
        print (e.message)
        print ('%s is ERROR !!!' % url)
        print ('server will be restart ')
        os.system('/etc/init.d/nginx restart')
        time.sleep(6)

if __name__ == '__main__':
#    print ('main')

#    def main():
        while True:
            opsrestart()



'''

python 命令行选项

-d   提供调试输出
-O 生成优化的字节码(生成 .pyo 文件)
-S  不导入 site 模块以在启动时查找 Python 路径
-v  冗余输出(导入语句详细追踪)
-m mod  将一个模块以脚本形式运行
-Q opt  除法选项(参阅文档)
-c cmd  运行以命令行字符串形式提交的 Python 脚本
file  从给定的文件运行 Python 脚本(参阅后文)














python 安装setuptools requests


wget https://bootstrap.pypa.io/ez_setup.py -O - | python

 wget https://bootstrap.pypa.io/ez_setup.py
pyht ez_setup.py

#官网https://pypi.python.org/pypi/setuptools#unix-wget


git clone git://github.com/kennethreitz/requests.git
cd requests/
 python setup.py  install


#官方#http://docs.python-requests.org/zh_CN/latest/user/quickstart.html


ImportError: No module named setuptools





















'''