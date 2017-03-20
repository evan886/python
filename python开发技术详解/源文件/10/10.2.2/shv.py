#!/usr/bin/python
# -*- coding: UTF-8 -*-

import shelve

addresses = shelve.open('addresses')
addresses['1'] = ['Tom', 'Beijing road', '2008-01-03']
addresses['2'] = ['Jerry', 'Shanghai road', '2008-03-30']
addresses['3'] = 3
#addresses['4'] = 0
if addresses.has_key('2'):
    del addresses['2']
print addresses
addresses.close()

