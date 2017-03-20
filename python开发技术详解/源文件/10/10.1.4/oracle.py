#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cx_Oracle

connection = cx_Oracle.connect("scott", "tiger", "ORCL")    # 连接oracle数据库
cursor = connection.cursor()                                # 获取cursor对象操作数据库
cursor.arraysize = 15
sql = """select a.ename 姓名,a.job 工作,a.sal 薪水,c.dname 部门,b.ename 管理者
        from emp a,emp b,dept c
        where a.sal > 2500
        and a.deptno = c.deptno
        and a.mgr = b.empno(+)
        order by a.sal"""
cursor.execute(sql)
for x in cursor.fetchall():
    for value in x:
        print value,
    print
cursor.close()
connection.close()