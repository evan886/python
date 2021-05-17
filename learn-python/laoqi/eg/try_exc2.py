#!/usr/bin/python3
# -*- coding: utf-8 -*-
while 1:
    print("this is a dvivsion program.")
    c=input("input 'c' continue, otherwise loguot:")
    if c == 'c':
        a = input("first num")
        b=input("second no.")
        try:
            print(float(a)/float(b))
            print("**********************")
        except ZeroDivisionError:
            print("This second num can't be zero")
            print("**************")
        except ValueError:
            print("please input no.")
            print("**********")
    else:
        break
