#!/usr/bin/python
# -*- coding: UTF-8 -*-

import win32com.client

engine = win32com.client.Dispatch("DAO.DBEngine.36")    # ʵ�������ݿ�����
db = engine.OpenDatabase("addresses.mdb")               # �����ݿ�����
rs = db.OpenRecordset("address")                        # ���ݱ������ؽ��������
rs = db.OpenRecordset("select * from address")          # ͨ��SQL��䷵�����ݼ�����
# ��������
db.Execute("""
insert into address(name, address, createtime) 
values('����', '�Ϻ����', '2008-3-25')
""")
while not rs.EOF:                                       # �����address�е�����
    print (rs.Fields("address").Value).encode('gb2312')
    rs.MoveNext()
