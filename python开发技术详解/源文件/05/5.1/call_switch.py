#!/usr/bin/python
# -*- coding: UTF-8 -*-

import switch_class

operator = "+"
x = 1
y = 2
for case in switch(operator):        # switchֻ������for inѭ����
    if case('+'):
        print x + y
        break
    if case('-'):
        print x - y
        break
    if case('*'):
        print x * y
        break
    if case('/'):
        print x / y
        break
    if case():                      # Ĭ�Ϸ�֧
        print ""

operator = "+"
x = 1
y = 2
for case in switch(operator):        # switchֻ������for inѭ����
    if case('+'):
        print x + y
    if case('-'):
        print x - y
    if case('*'):
        print x * y
        break
    if case('/'):
        print x / y
        break
    if case():                      # Ĭ�Ϸ�֧
        print ""