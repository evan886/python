#!/usr/bin/python
# -*- coding: UTF-8 -*-
# ������ģ��������������
# Filename: ruleModule.py

_rule = "rule information"

#��������е���������
class Student:                      # ������д
    __name = ""                     # ˽��ʵ������ǰ�����������»���
    def __init__(self, name):
        self.__name = name          # self�൱��Java�е�this
    def getName(self):              # ����������ĸСд�����ÿ�����ʵ�����ĸ��д
        return self.__name

if __name__ == "__main__":
    student = Student("borphi")     # ������Сд
    print student.getName()
# �����е���������
import random

def compareNum(num1, num2):
    if(num1 > num2):
        return 1
    elif(num1 == num2):
        return 0
    else:
        return -1
num1 = random.randrange(1, 9, 2)
num2 = random.randrange(1, 9, 2)
print "num1 =", num1
print "num2 =", num2
print compareNum(num1, num2)
  
# ���淶�ı�������
sum = 0
i = 2000
j = 1200
sum = i + 12 * j
# �淶�ı�������
sumPay = 0
bonusOfYear = 2000
monthPay = 1200
sumPay = bonusOfYear + 12 * monthPay