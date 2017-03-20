#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

try:
    x = 10 / 0
except Exception, ex:
    print ex
    print sys.exc_info()


