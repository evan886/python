#!/usr/bin/python
# -*- coding: UTF-8 -*-
i = 1
while i > 0:
    i = i + 1
    print i
    
# whileѭ��
numbers = raw_input("���뼸�����֣��ö��ŷָ���").split(",")
print numbers
x = 0
while x < len(numbers):                   
    print numbers[x]
    x += 1

# ��else�Ӿ��whileѭ��
x = input("����x��ֵ��")
i = 0
while(x <> 0):   
    if(x > 0):
        x -= 1
    else:
        x += 1
    i = i + 1
    print "��%d��ѭ����" %i, x
else:
    print "x����0��", x
