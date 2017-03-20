#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 变量、模块名的命名规则
# Filename: ruleModule.py

_rule = "rule information"

#面向对象中的命名规则
class Student:                      # 类名大写
    __name = ""                     # 私有实例变量前必须有两个下划线
    def __init__(self, name):
        self.__name = name          # self相当于Java中的this
    def getName(self):              # 方法名首字母小写，其后每个单词的首字母大写
        return self.__name

if __name__ == "__main__":
    student = Student("borphi")     # 对象名小写
    print student.getName()
# 函数中的命名规则
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
  
# 不规范的变量命名
sum = 0
i = 2000
j = 1200
sum = i + 12 * j
# 规范的变量命名
sumPay = 0
bonusOfYear = 2000
monthPay = 1200
sumPay = bonusOfYear + 12 * monthPay