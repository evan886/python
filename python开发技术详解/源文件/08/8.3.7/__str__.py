#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Fruit:      
    '''Fruit��'''
    def __str__(self):          # ���������ַ�����ʾ
        return self.__doc__

if __name__ == "__main__":
    fruit = Fruit()
    print str(fruit)            # ����__str__
    print fruit
