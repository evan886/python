#!/usr/bin/python
import re
line = "Cats are smarter than dogs"

searchObj = re.search(r'(.*) are (.*?) than (.*).*', line ,re.M|re.I)

if searchObj:
    print "searchObj.group():" , searchObj.group()
    print "searchObj.group(1):" , searchObj.group(1)
    print "searchObj.group(2):" , searchObj.group(2)
    print "searchObj.group(3):" , searchObj.group(3)
