#!/usr/bin/python
# -*- coding: UTF-8 -*-

import win32com.client

conn = win32com.client.Dispatch('ADODB.Connection')     # ʵ�������ݿ����Ӷ���
dsn = 'Provider=OraOLEDB.Oracle;PLSQLRSet=1;Password=tiger;User ID=scott;Data Source=ORCL'
conn.Open(dsn)                                          # ��oracle���ݿ�
rs = win32com.client.Dispatch('ADODB.Recordset')
sql = """select a.ename ����,a.job ����,a.sal нˮ,c.dname ����,b.ename ������
        from emp a,emp b,dept c
        where a.sal > 2500
        and a.deptno = c.deptno
        and a.mgr = b.empno(+)
        order by a.sal"""
rs.Open(sql, conn)                                      # ���ز�ѯ�Ľ����
li = list()
rs.MoveFirst()
while not rs.EOF:
    d = dict()
    for x in range(rs.Fields.Count):                    # ��ÿ�����ݴ洢��һ���ֵ���
        key = rs.Fields.Item(x).Name
        value = rs.Fields.Item(x).Value
        d.setdefault(key, value)                        # �����ֶ������ֶ�ֵ�Ķ�Ӧ��ϵ
    li.append(d)                                        # ��ÿ���ֵ�洢���б���
    print rs.Fields("нˮ").Value, rs.Fields("����").Value, \
          rs.Fields("����").Value, rs.Fields("����").Value, \
          rs.Fields("������").Value
    rs.MoveNext()
for d in li:                                            # ����б��е�����
    for key in d.keys():       
        print key.encode("gb2312"), d.get(key),
    print
conn.Close()                                            # �ر�����

