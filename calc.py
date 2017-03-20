#!/usr/bin/python
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#print calc(1,2)
nums = [1,2,3]
print calc(*nums)
