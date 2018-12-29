
http://192.168.30.56
use dkm
password dkm123456



注意  
sudo python manage.py  runserver 0.0.0.0:80 运行 可能会 
AttributeError at /
class Meta has no attribute 'object_class'

怎么样才能搞成可以用 80端口的呢  



#HCMDB
### 目前拥有功能有：
####资产管理
    * 根据不同数据中心(IDC),分类管理
    * 支持导出excel文件

####应用管理
  
####域名管理
  	* 输入域名自动获取域名信息

####用户管理
    * 根据不同需求设置用户可访问该系统的那些菜单

####告警接口
    * 接口使用请看alarm/readme

##安装环境






wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py

yum install  python-devel


ImportError No module named MySQLdb解决方法
pip install mysql-python

[root@localhost hcmdb]# pip install MySQL-python
Collecting MySQL-python
  Using cached MySQL-python-1.2.5.zip
    Complete output from command python setup.py egg_info:
    sh: mysql_config: 未找到命令

source  /etc/profile #就可以了 哈哈






清空数据库
python manage.py flush

* python2.7
* pip install -r requirements.txt

##初始化
###初始数据库
####创建数据库(进入数据库操作)
    #* create database hcmdb CHARACTER SET utf8;
    * create database mycmdb CHARACTER SET utf8;
    grant all on mycmdb.* to mycmdb@'localhost' identified by 'evan886DKdk****#d'; (根据settings.py中设定修改)
    #* grant all on hcmdb.* to HCmdbAdmin@'localhost' identified by 'nDrDyXd#dnoMqH2'; (根据settings.py中设定修改)
####初始化数据表
    * python2.7 manage.py makemigrations
    * python2.7 manage.py migrate

####初始化数据  我一般 是导入为自己的
    mysql -umycmdb -p mycmdb < hcmdb20170926.sql
    #* mysql -uHCmdbAdmin -p hcmdb < init.sql

##运行 为什么 有一次用 80 和sudo 不行呢 
   * python2.7 manage.py runserver 0.0.0.0:8888

##登陆
   * 用户名: cmdbAdmin
	 密码: cmdbAdmin

#err 395292

  File "/usr/lib/python2.7/dist-packages/MySQLdb/connections.py", line 50, in defaulterrorhandler
    raise errorvalue
django.db.utils.OperationalError: (1005, 'Can\'t create table `hcmdb`.`#sql-19cb_39` (errno: 150 "Foreign key constraint is incorrectly formed")')


