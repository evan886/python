#!/usr/bin/python
# -*- coding: UTF-8 -*-

# try...except
try:
    file("hello.txt", "r")
    print "读文件"
except IOError:                 # 捕获IOError异常
    print "文件不存在"
except:                         # 其他异常情况
    print "程序异常"

# try...except...else
try:
    result = 10/0
except ZeroDivisionError:
    print "0不能被整除"        
else:                                   
    print result


# try...except的嵌套
try:                                
    s = "hello"
    try:                           
        print s[0] + s[1]
        print s[0] - s[1]
    except TypeError:                     
        print "字符串不支持减法运算"
except:
    print "异常"

    #TypeError: 'str' object does not support item assignment
    


