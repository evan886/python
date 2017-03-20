#!/usr/bin/python
# -*- coding: UTF-8 -*-

# os.walk±éÀúÄ¿Â¼
import os

def VisitDir(path):
    for root,dirs,files in os.walk(path,True):
        for filepath in files:
            print os.path.join(root, filepath)

if __name__=="__main__":
    path = r"D:\developer\python\example\07"
    VisitDir(path)
