#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 自定义模块
from copy import deepcopy
count = 1

def func():
    global count
    count = count + 1
    return count
