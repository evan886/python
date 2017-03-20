#!/usr/bin/python
# -*- coding: UTF-8 -*-
import dbhash

db = dbhash.open('temp', 'c')               # 创建并打开数据库
db['Tom'] = 'Beijing road'                  # 写数据
db['Jerry'] = 'Shanghai road'
for k, v in db.iteritems():                 # 遍历db对象
    print k, v
if db.has_key('Tom'):
    del db['Tom']
db['Tod'] = 2                               # 非字符串的键或值会引发异常
print db
db.close()                                  # 关闭数据库
