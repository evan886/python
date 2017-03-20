#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sqlite3

# �������ݿ�
conn = sqlite3.connect("D:/developer/python/example/10/addresses.db")
# ������
conn.execute("create table if not exists address(id integer primary key autoincrement, name varchar(128), address varchar(128))")
# ��������
conn.execute("insert into address(name, address) values ('Tom', 'Beijing road')")
conn.execute("insert into address(name, address) values ('Jerry', 'Shanghai road')")
# �ֶ��ύ����
conn.commit()
# ��ȡ�α����
cur = conn.cursor()
# ʹ���α��ѯ����
cur.execute("select * from address")
# ��ȡ���н��
res = cur.fetchall()
print "address: ", res
for line in res:
    for f in line:
        print f,
    print
# �ر�����
cur.close()
conn.close()
