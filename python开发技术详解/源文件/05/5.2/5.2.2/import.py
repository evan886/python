#!/usr/bin/python
# -*- coding: UTF-8 -*-

import myModule        
print "count =", myModule.func()           
myModule.count = 10
print "count =", myModule.count

import myModule 
print "count =", myModule.func() 

# import�������������
if myModule.count > 1:
    myModule.count = 1    
else:
    import myModule
print "count =", myModule.count
