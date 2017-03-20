#!/usr/bin/python
# -*- coding: UTF-8 -*-

import win32com.client

engine = win32com.client.Dispatch("DAO.DBEngine.36")    # 实例化数据库引擎
db = engine.OpenDatabase("addresses.mdb")               # 打开数据库连接
rs = db.OpenRecordset("address")                        # 根据表名返回结果集对象
rs = db.OpenRecordset("select * from address")          # 通过SQL语句返回数据集对象
# 插入数据
db.Execute("""
insert into address(name, address, createtime) 
values('赵涛', '上海虹口', '2008-3-25')
""")
while not rs.EOF:                                       # 输出表address中的数据
    print (rs.Fields("address").Value).encode('gb2312')
    rs.MoveNext()
