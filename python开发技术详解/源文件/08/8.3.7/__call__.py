#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Fruit:
    class Growth:        # 内部类
        def __call__(self):
            print "grow ..."

    grow = Growth()       # 返回__call__的内容

if __name__ == '__main__':
    fruit = Fruit()
    fruit.grow()
    Fruit.grow()