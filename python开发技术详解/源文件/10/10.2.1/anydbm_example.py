#!/usr/bin/python
# -*- coding: UTF-8 -*-
import dbhash

db = dbhash.open('temp', 'c')               # �����������ݿ�
db['Tom'] = 'Beijing road'                  # д����
db['Jerry'] = 'Shanghai road'
for k, v in db.iteritems():                 # ����db����
    print k, v
if db.has_key('Tom'):
    del db['Tom']
db['Tod'] = 2                               # ���ַ����ļ���ֵ�������쳣
print db
db.close()                                  # �ر����ݿ�
