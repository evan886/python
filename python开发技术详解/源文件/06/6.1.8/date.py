#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time,datetime

# ʱ�䵽�ַ�����ת��
print time.strftime("%Y-%m-%d %X", time.localtime())
# �ַ�����ʱ���ת��
t = time.strptime("2008-08-08", "%Y-%m-%d")
y, m, d = t[0:3]
print datetime.datetime(y, m, d)

