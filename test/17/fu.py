#!/usr/bin/python
x = 'I am global  var'

def fun():

    global y
    y = 200
    
    global x
    x = 100

fun()    
print x
