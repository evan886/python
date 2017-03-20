#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sqlite3

# 连接数据库
conn = sqlite3.connect("D:/developer/python/example/10/addresses.db")
# 创建表
conn.execute("create table if not exists address(id integer primary key autoincrement, name varchar(128), address varchar(128))")
# 插入数据
conn.execute("insert into address(name, address) values ('Tom', 'Beijing road')")
conn.execute("insert into address(name, address) values ('Jerry', 'Shanghai road')")
# 手动提交数据
conn.commit()
# 获取游标对象
cur = conn.cursor()
# 使用游标查询数据
cur.execute("select * from address")
# 获取所有结果
res = cur.fetchall()
print "address: ", res
for line in res:
    for f in line:
        print f,
    print
# 关闭连接
cur.close()
conn.close()
