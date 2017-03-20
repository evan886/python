#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 重定向输出
import sys

sys.stdout = open(r"./hello.txt","a")
print "goodbye"
sys.stdout.close()

  