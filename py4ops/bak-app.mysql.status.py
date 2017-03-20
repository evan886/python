#!/usr/bin/python
# -*- coding: utf8 -*-
# Author :
# Date : 2017/1/17
# 说明：mysql性能监控,script_name: MysqlMonior.py

import os,re,sys,re,base64,time,commands

class MysqlMonior:
    """
    #使用说明：从库实例使用的端口列表写在下面,用英文逗号,分隔开
    """
    def __init__(self):
        """
        #初始化值
        """
        self.keyvalues = {}
        self.dbport = sys.argv[1]
        self.dbitem = sys.argv[2]
        self.sock = '/data/db/mysql/mysql_%s.sock'% self.dbport
        self.dbpassfile = '/data/app/scripts/.pass.cnf' 
        self.conf = '--defaults-extra-file=%s -S %s' % (self.dbpassfile,self.sock)
        self.mysqlbin = "sudo /data/apps/mysql/bin/mysql %s -e "% self.conf
        self.mysqldumpbin = "sudo /data/apps/mysql/bin/mysqladmin %s"% self.conf  
        if int(self.dbport) == 3306 :
            self.datadir = "/data/db/mysql"
        else :
            self.datadir = "/data/db/mysql_%s"% self.dbport
        self.mysqlStatus = ['Com_insert', 'Com_delete', 'Com_select', 'Com_update', 'Slow_queries', \
            'Com_replace', 'Threads_connected', 'max_connections', 'total_size', 'Created_tmp_disk_tables', \
            'innodb_buffer_pool_size', 'Open_files', 'Opened_tables', 'open_files_limit', 'Threads_running', \
            'Seconds_Behind_Master', 'Slave_IO_Running', 'Slave_SQL_Running']

    def getMsqlStatus(self, cmd, sep='\s+', kidx=0, vidx=1):
        """
        #说明：获取mysql的所有信息，生成字典格式
        """
        keyvalues = {}
        with os.popen(cmd) as f:
            for line in f.readlines():
                tmp = re.split(sep, line, vidx)
                if len(tmp) > vidx :
                    keyvalues[tmp[kidx].strip()] = tmp[vidx].strip()
        return keyvalues

    def getMsqlMonior(self):
        """
        #说明：获取mysql指定的监控信息
        """
        #获取mysql的数据大小
        getmysqlSize = "sudo du -sb %s " % self.datadir
        keyvalue = self.getMsqlStatus(getmysqlSize, '\s+',0,0);
        if len(keyvalue) == 1:
            self.keyvalues['total_size'] = keyvalue.values()[0] 
        
        #获取mysql的全局状态
        cmd1 = "show variables;show global status;"
        getstatuscmd = "%s \"%s\""% (self.mysqlbin, cmd1) 
        self.keyvalues.update(self.getMsqlStatus(getstatuscmd))
        
        #获取mysql的从库状态
        cmd2 = "show slave status\G"
        showslave = "%s \" %s\""% (self.mysqlbin, cmd2)        
        self.keyvalues.update(self.getMsqlStatus(showslave, ':' ))
    
        #获取mysql的extended-status状态
        cmd3 = "extended-status;"
        showextend = "%s %s"%(self.mysqldumpbin,cmd3)
        self.keyvalues.update(self.getMsqlStatus(showextend, '|', 1, 2))
        return self.keyvalues


if __name__ == '__main__':
    if len(sys.argv) < 2 :
        print 'python %s sys.argv[1] sys.argv[2]'%sys.argv[0]
        sys.exit(0)
    #判断进程是否已经启动，如果启动，就不再重复启动
    comm1 = "ps -ef|grep 'python /etc/zabbix/scripts/app.mysql.status.py'|grep -v grep|wc -l"
    status,output = commands.getstatusoutput(comm1)
    if int(output) >= 3 :
        print("YYyunwei: dbrelease_doing.py is running...")
        sys.exit(0)
    yyMysql = MysqlMonior()
    mysqlDict = yyMysql.getMsqlMonior()
    if int(sys.argv[1]) == 3306 :
        mysqlDict.update({'Seconds_Behind_Master':0,'Slave_IO_Running':'Yes','Slave_SQL_Running':'Yes'})
    if sys.argv[2] in ['Slave_IO_Running','Slave_SQL_Running'] :
        print mysqlDict[sys.argv[2]]
    else :
        print int(mysqlDict[sys.argv[2]])
    #for yyMysql.dbitem in yyMysql.mysqlStatus :
    #    #if status == "status Slave_IO_Running" and yyMysql.mysqlStatus[status] == "Yes" :
    #        
    #    if status in mysqlDict.keys() :
    #        print "mysql status %s : %s "% (status, mysqlDict[status])
    #    else :
    #        print "mysql status %s : "% status
