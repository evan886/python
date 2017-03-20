#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cx_Oracle

connection = cx_Oracle.connect("scott", "tiger", "ORCL")    # ����oracle���ݿ�
cursor = connection.cursor()                                # ��ȡcursor����������ݿ�
cursor.arraysize = 15
sql = """select a.ename ����,a.job ����,a.sal нˮ,c.dname ����,b.ename ������
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