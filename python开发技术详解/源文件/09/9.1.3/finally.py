#!/usr/bin/python
# -*- coding: UTF-8 -*-

# finally������÷�
#try:
#    f = file("hello2.txt", "r")
#    print "���ļ�"
#except IOError:						    # ����IOError�쳣
#    print "�ļ�������"
#finally:    						        # �����쳣���
#    f.close()


# try...except...finally
try:                                
    f = open("hello.txt", "r") 
    try:                 
        print fsock.read(5)
    except:
        print "��ȡ�ļ�����"
    finally:                            # finally�Ӿ�һ�������ͷ���Դ
        print "�ͷ���Դ"    
        f.close()
except IOError: 
    print "�ļ�������" 
