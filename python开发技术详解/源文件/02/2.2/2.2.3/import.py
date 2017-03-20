#!/usr/bin/python
# -*- coding: UTF-8 -*-

#规范导入方式
import sys

print sys.path
print sys.argv

#不规范导入方式
from sys import path
from sys import argv

print path
print argv
