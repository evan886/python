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
* python2.7
* pip install -r requirements.txt

##初始化
###初始数据库
####创建数据库(进入数据库操作)
    * create database hcmdb;
    * grant all on hcmdb.* to HCmdbAdmin@'localhost' identified by 'nDrDyXd#dnoMqH2'; (根据settings.py中设定修改)
####初始化数据表
    * python2.7 manage.py makemigrations
    * python2.7 manage.py migrate

####初始化数据
    * mysql -uHCmdbAdmin -p hcmdb < init.sql

##运行
   * python2.7 manage.py runserver 0.0.0.0:9003

##登陆
   * 用户名: cmdbAdmin
	 密码: cmdbAdmin
