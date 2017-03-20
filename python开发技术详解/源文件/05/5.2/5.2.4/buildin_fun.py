#!/usr/bin/python
# -*- coding: UTF-8 -*-

# apply()
def sum(x=1, y=2):
    return x + y

print apply(sum, (1, 3))

# filter()
def func(x): 
    if x > 0:
        return x

print filter(func, range(-9, 10))


# reduce()
def sum(x, y):
    return x + y
print reduce(sum, range(0, 10))
print reduce(sum, range(0, 10), 10)
print reduce(sum, range(0, 0), 10)

# map()
def power(x): return x ** x           
print map(power, range(1, 5)) 
def power2(x, y): return x ** y   
print map(power2, range(1, 5), range(5, 1, -1))  
