#!/usr/bin/python
# -*- coding: UTF-8 -*-

# try...except
try:
    file("hello.txt", "r")
    print "���ļ�"
except IOError:                 # ����IOError�쳣
    print "�ļ�������"
except:                         # �����쳣���
    print "�����쳣"

# try...except...else
try:
    result = 10/0
except ZeroDivisionError:
    print "0���ܱ�����"        
else:                                   
    print result


# try...except��Ƕ��
try:                                
    s = "hello"
    try:                           
        print s[0] + s[1]
        print s[0] - s[1]
    except TypeError:                     
        print "�ַ�����֧�ּ�������"
except:
    print "�쳣"

    #TypeError: 'str' object does not support item assignment
    


