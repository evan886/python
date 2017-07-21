#!/usr/bin/python
import time 
s = "hello"
l = [1,2,3,'a','b']
t = (7,8,9,'x','y')
d = {1:111,2:222,5:555,3:333}


for x in range(1,11):
    print x
    if x == 6:
        break
else:
    print "1ending"

for x in range(1,11):
    print "----->", x
