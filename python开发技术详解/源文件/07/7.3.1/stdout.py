#!/usr/bin/python
# -*- coding: UTF-8 -*-

# �ض������
import sys

sys.stdout = open(r"./hello.txt","a")
print "goodbye"
sys.stdout.close()

  