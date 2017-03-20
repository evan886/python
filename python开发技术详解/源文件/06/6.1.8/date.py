#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time,datetime

# 时间到字符串的转换
print time.strftime("%Y-%m-%d %X", time.localtime())
# 字符串到时间的转换
t = time.strptime("2008-08-08", "%Y-%m-%d")
y, m, d = t[0:3]
print datetime.datetime(y, m, d)

