#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Fruit:
    def __init__(self):
        self.__color = "red"

class Apple(Fruit):             # Apple�̳���Fruit
    pass
        
if __name__ == "__main__":
    fruit = Fruit()
    apple = Apple()
    print Apple.__bases__       # ���������ɵ�Ԫ��
    print apple.__dict__        # ���������ɵ��ֵ�
    print apple.__module__      # ��������ڵ�ģ����
    print apple.__doc__         # ���doc�ĵ�



