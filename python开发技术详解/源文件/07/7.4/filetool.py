#!/usr/bin/python
# -*- coding: UTF-8 -*-

def showFileProperties(path):
    '''��ʾ�ļ������ԡ�����·������С���������ڡ�����޸�ʱ�䣬������ʱ��'''
    import time,os
    for root,dirs,files in os.walk(path,True):
        print "λ�ã�" + root
        for filename in files:
            state = os.stat(os.path.join(root, filename))
            info = "�ļ���: " + filename + " " 
            info = info + "��С��" + ("%d" % state[-4]) + " "
            t = time.strftime("%Y-%m-%d %X", time.localtime(state[-1]))
            info = info + "����ʱ�䣺" + t + " "
            t = time.strftime("%Y-%m-%d %X", time.localtime(state[-2]))
            info = info + "����޸�ʱ�䣺" + t + " "
            t = time.strftime("%Y-%m-%d %X", time.localtime(state[-3]))
            info = info + "������ʱ�䣺" + t + " "
            print info

if __name__ == "__main__":
    path = r"D:\developer\python\example\07\7.2.2"
    showFileProperties(path)
