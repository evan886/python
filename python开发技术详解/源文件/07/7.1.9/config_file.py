#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 读配置文件
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("ODBC.ini")
sections = config.sections()                    # 返回所有的配置块
print "配置块：", sections
o = config.options("ODBC 32 bit Data Sources")  # 返回所有的配置项
print "配置项：", o
v = config.items("ODBC 32 bit Data Sources")
print "内容：", v
# 根据配置块和配置项返回内容
access = config.get("ODBC 32 bit Data Sources", "MS Access Database")
print access
excel = config.get("ODBC 32 bit Data Sources", "Excel Files")
print excel
dBASE = config.get("ODBC 32 bit Data Sources", "dBASE Files")
print dBASE

# 写配置文件
import ConfigParser

config = ConfigParser.ConfigParser()
config.add_section("ODBC Driver Count")             # 添加新的配置块
config.set("ODBC Driver Count", "count", 2)         # 添加新的配置项
f = open("ODBC.ini", "a+")
config.write(f)                                 
f.close()

# 修改配置文件
import ConfigParser
config = ConfigParser.ConfigParser()
config.read("ODBC.ini")
config.set("ODBC Driver Count", "count", 3)
f = open("ODBC.ini", "r+")
config.write(f)     
f.close()

# 删除配置文件
import ConfigParser
config = ConfigParser.ConfigParser()
config.read("ODBC.ini")
config.remove_option("ODBC Driver Count", "count")  # 删除配置项
config.remove_section("ODBC Driver Count")          # 删除配置块
f = open("ODBC.ini", "w+")
config.write(f)     
f.close()


