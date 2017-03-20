#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
print sys.modules.keys()
print sys.modules.values()
print sys.modules["os"]

import sys
d = sys.modules.copy()
import copy,string
print zip(set(sys.modules) - set(d))




    

