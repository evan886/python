#!/usr/bin/python3
# -*- coding: utf-8 -*-
while 1:
        try:
            a=input("firest  no.")
            b=input("second no.")
            r=(float(a)/float(b))
            print(r)
        except Exception as e:
            print(e)
            print("try again")
        else:
            break
