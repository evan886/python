#!/usr/bin/python
# -*- coding: UTF-8 -*-

import exceptions
try:
    s = None
    if s is None:    
        print "s�ǿն���"
        raise NameError
    print len(s)
except TypeError:
    print "�ն���û�г���"

print help(exceptions)

