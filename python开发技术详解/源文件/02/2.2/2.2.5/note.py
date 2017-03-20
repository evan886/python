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

# 规范的变量命名
sumPay = 0                                  # 年薪
bonusOfYear = 2000                          # 年终奖金
monthPay = 1200                             # 月薪
sumPay = bonusOfYear + 12 * monthPay        # 年薪 = 年终奖金 + 12 * 月薪


# 注释在调试程序中的作用
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