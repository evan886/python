#!/usr/bin/python
# -*- coding: UTF-8 -*-

import win32com.client

conn = win32com.client.Dispatch('ADODB.Connection')     # 实例化数据库连接对象
dsn = 'Provider=OraOLEDB.Oracle;PLSQLRSet=1;Password=tiger;User ID=scott;Data Source=ORCL'
conn.Open(dsn)                                          # 打开oracle数据库
rs = win32com.client.Dispatch('ADODB.Recordset')
sql = """select a.ename 姓名,a.job 工作,a.sal 薪水,c.dname 部门,b.ename 管理者
        from emp a,emp b,dept c
        where a.sal > 2500
        and a.deptno = c.deptno
        and a.mgr = b.empno(+)
        order by a.sal"""
rs.Open(sql, conn)                                      # 返回查询的结果集
li = list()
rs.MoveFirst()
while not rs.EOF:
    d = dict()
    for x in range(rs.Fields.Count):                    # 把每行数据存储在一个字典中
        key = rs.Fields.Item(x).Name
        value = rs.Fields.Item(x).Value
        d.setdefault(key, value)                        # 建立字段名和字段值的对应关系
    li.append(d)                                        # 把每个字典存储在列表中
    print rs.Fields("薪水").Value, rs.Fields("工作").Value, \
          rs.Fields("部门").Value, rs.Fields("姓名").Value, \
          rs.Fields("管理者").Value
    rs.MoveNext()
for d in li:                                            # 输出列表中的内容
    for key in d.keys():       
        print key.encode("gb2312"), d.get(key),
    print
conn.Close()                                            # 关闭连接

