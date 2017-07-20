#!/usr/bin/python
s = "hello"
l = [1,2,3,'a','b']
t = (7,8,9,'x','y')
d = {1:111,2:222,5:555,3:333}


for x in d:
    print d[x]
else:
    print "1ending"

for k,v in d.items():
    print k
    print v
else:
    print "en"
