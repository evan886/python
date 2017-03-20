#!/usr/bin/python
#-*- coding:utf-8 -*-

import MySQLdb
import sys

class check_mysql_slave:
    def __int__(self):
        self.dbhost = 'localhost'
        self.dbuser = 'root'
        self.dbpass = 'evan'
        self.dbport = 3306
        self.sock = " /tmp/mysql.sock"

        self.conn=MySQLdb.connect(unix_socket=self.sock)
        self.cursor=self.conn.cursor(cursorclass  = MySQLdb.cursors.DictCursor)
        self.sql = 'show slave status'
        self.cursor.execute(self.sql)
        self.data = self.cursor.fetchall()
        self.io = self.data[0] ['Slave_IO_Runnig']
        self.sql = self.data[0] ['Slave_SQL_Runnig']
        self.conn.close()

    def get_io_status(self):
        if self.io == 'Yes':
            return 1
        else:
            return 0

    def get_sql_status(self):
        if self.sql == 'Yes':
            return 1
        else:
            return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: %s [io|sql]" % sys.argv[0]
        sys.exit(1)
    mysql = check_mysql_slave()
    if sys.argv[1] == "io":
        print mysql.get_io_status()
    elif sys.argv[1] == "sql":
        print mysql.get_sql_status()

"""
yum install MySQL-python

>>> import MySQLdb
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named MySQLdb


--socket=/tmp/mysql.sock --port=3306

root@abroad_db2 ~]# ps -ef | grep mysql
root      4441  4240  0 16:03 pts/1    00:00:00 grep mysql
root      8191     1  0  2016 ?        00:00:00 /bin/sh /data/apps/mysql/bin/mysqld_safe --datadir=/data/apps/mysql/data --pid-file=/data/apps/mysql/data/abroad_db2.pid
mysql     9066  8191  1  2016 ?        1-17:43:38 /data/apps/mysql/bin/mysqld --basedir=/data/apps/mysql --datadir=/data/apps/mysql/data --plugin-dir=/data/apps/mysql/lib/plugin --user=mysql --log-error=/data//logs/mysql/mysqld-error.log --pid-file=/data/apps/mysql/data/abroad_db2.pid --socket=/tmp/mysql.sock --port=3306


"""