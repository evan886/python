#!/usr/bin/python
# -*- coding: UTF-8 -*-

import odbc, dbi                              # ����ODBCģ�����������
import time

db = odbc.odbc('addresses/scott/tiger')      # �����ݿ�����
curser = db.cursor()                         # ����cursor�α�
curser.execute("select * from address order by id desc")
for col in curser.description:                # ��ʾ������
    print col[0], col[1]
result = curser.fetchall()
for row in result:                            # ������ֶε�ֵ
    print row
    print row[1], row[2]
    timeTuple = time.localtime(row[3])
    print time.strftime('%Y/%m/%d', timeTuple)
