#!/usr/bin/python
# -*- coding: UTF-8 -*-

# note - show Python's note
# Copyright (C) 2008 bigmarten
#
# This program is free software. you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation
#
########################################################################
#
# Version is 1.0
#
# Its contents are calculate payment.
#
########################################################################

# �淶�ı�������
sumPay = 0                                  # ��н
bonusOfYear = 2000                          # ���ս���
monthPay = 1200                             # ��н
sumPay = bonusOfYear + 12 * monthPay        # ��н = ���ս��� + 12 * ��н


# ע���ڵ��Գ����е�����
def compareNum(num1, num2):
    if(num1 > num2):
        return str(num1)+" > "+str(num2)
    elif(num1 < num2):
        return str(num1)+" < "+str(num2)
    elif(num1 == num2):
        return str(num1)+" = "+str(num2)
    else:
        return ""
num1 = 2
num2 = 1
print compareNum(num1, num2)
num1 = 2
num2 = 2
print compareNum(num1, num2)
num1 = 1
num2 = 2
print compareNum(num1, num2)