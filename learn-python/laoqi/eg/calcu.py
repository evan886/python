#!/usr/bin/python3
# -*- coding: utf-8 -*-
class Calculator(object):
    #is_raise = False
    is_raise =True
    def calc(self,express):
        try:
            return eval(express)
        except ZeroDivisionError:
            if self.is_raise:
                return "zero cat not be division."
            else:
                raise
if __name__ == "__main__":
    c=Calculator()
    print(c.calc("8/0"))
