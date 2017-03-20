#!/usr/bin/python
# -*- coding: UTF-8 -*-

# if elif elseÓï¾ä
score = input("score:")
if(score >= 90) and (score <= 100):
    print "A"
elif(score >= 80) and (score < 90):
    print "B"
elif(score >= 60) and (score < 80):
    print "C"
else:
    print "D"