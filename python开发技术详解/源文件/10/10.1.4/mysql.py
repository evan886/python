#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
import MySQLdb
# �������ݿ�
try:
    conn = MySQLdb.connect(host='localhost',user='root',passwd='',db='ADDRESSBOOKDB')       
except Exception, e:
    print e
    sys.exit()
cursor = conn.cursor()
sql = "insert into address(name, address) values (%s, %s)" 
values  = (("����", "����������"), ("����", "����������"), ("����", "����������"))
try:
    cursor.executemany(sql, values)        # �����������
except Exception, e:
    print e
sql = "select * from address"
cursor.execute(sql)                     # ��ѯ����
data = cursor.fetchall()
if data:
    for x in data:
        print x[0], x[1]
cursor.close()                          # �ر��α�
conn.close()                            # �ر����ݿ�

# ת���ַ�����
s = "escape''"
print s
print MySQLdb.escape_string(s)
