#!/usr/bin/python
# -*- coding: UTF-8 -*-

# break���
x = input("����x��ֵ��")
y = 0
for y in range(0, 100):
    if x == y:
        print "�ҵ����֣�", x
        break
else:
    print "û���ҵ�"