#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Fruit:
    class Growth:        # �ڲ���
        def __call__(self):
            print "grow ..."

    grow = Growth()       # ����__call__������

if __name__ == '__main__':
    fruit = Fruit()
    fruit.grow()
    Fruit.grow()