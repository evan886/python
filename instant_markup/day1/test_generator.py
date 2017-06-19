#!/usr/bin/python
def func():
    yield 0
    yield  1
    yield 2

for i in func():
    print i

'''
python test_generator.py 
0
1
2

'''

