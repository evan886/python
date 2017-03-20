#!/usr/bin/python
# -*- coding: UTF-8 -*-

#from DBUtils.PooledDB import PooledDB
import DBUtils.PooledDB
import MySQLdb

pool = DBUtils.PooledDB(MySQLdb, 5,host = "localhost", user = "root", passwd = "", db = "ADDRESSBOOKDB") 
"""
PooledDB的第一个参数是creator: either an arbitrary function returning new DB-API 2 
        connection objects or a DB-API 2 compliant database module
也就是说，我们传入一个数据库实现类的module名字即可，它自己会去判断如何建立数据库连接。
"""
db_conn = pool.connection() # 这就是从连接池中获取一个连接的语句 