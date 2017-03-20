#!/usr/bin/python
# -*- coding: UTF-8 -*-

# finally错误的用法
#try:
#    f = file("hello2.txt", "r")
#    print "读文件"
#except IOError:						    # 捕获IOError异常
#    print "文件不存在"
#finally:    						        # 其他异常情况
#    f.close()


# try...except...finally
try:                                
    f = open("hello.txt", "r") 
    try:                 
        print fsock.read(5)
    except:
        print "读取文件错误"
    finally:                            # finally子句一般用于释放资源
        print "释放资源"    
        f.close()
except IOError: 
    print "文件不存在" 
