#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import division

class DivisionException(Exception):                 # �Զ����쳣
    def __init__(self, x, y):
        Exception.__init__(self, x, y)
        self.x = x
        self.y = y

if __name__ == "__main__":
    try:
        x = 3
        y = 2                         
        if x % y > 0:
            print x / y  
            raise DivisionException(x, y)           # �׳��쳣
    except DivisionException, div:
        print "DivisionException: x / y = %.2f" % (div.x / div.y)
