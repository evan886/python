#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 下面两条语句是等价的
print "hello world!"
print "hello world!";
# 使用分号分隔语句
x = 1; y = 1; z = 1
# 一条语句写在多行
print \
"hello world!"
# 字符串的换行
# 写法一
sql = "select id,name \
from dept \
where name = 'A'"
print sql
# 写法二
sql = "select id,name " \
      "from dept " \
      "where name = 'A'"
print sql