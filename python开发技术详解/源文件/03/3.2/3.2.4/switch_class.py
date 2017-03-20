#!/usr/bin/python
# -*- coding: UTF-8 -*-

class switch(object):
    def __init__(self, value):      # ��ʼ����Ҫƥ���ֵvalue
        self.value = value
        self.fall = False           # ���ƥ�䵽��case�����û��break����fallΪtrue��

    def __iter__(self):
        yield self.match            # ����match���� ����һ��������
        raise StopIteration         # StopIteration �쳣���ж�forѭ���Ƿ����

    def match(self, *args):         # ģ��case�Ӿ�ķ���
        if self.fall or not args:   # ���fallΪtrue�������ִ�������case�Ӿ�
                                    # ��case�Ӿ�û��ƥ�������ת��Ĭ�Ϸ�֧��
            return True
        elif self.value in args:    # ƥ��ɹ�
            self.fall = True
            return True
        else:                       # ƥ��ʧ��
            return False

operator = "+"
x = 1
y = 2
for case in switch(operator):        # switchֻ������for inѭ����
    if case('+'):
        print x + y
        break
    if case('-'):
        print x - y
        break
    if case('*'):
        print x * y
        break
    if case('/'):
        print x / y
        break
    if case():                      # Ĭ�Ϸ�֧
        print ""

operator = "+"
x = 1
y = 2
for case in switch(operator):        # switchֻ������for inѭ����
    if case('+'):
        print x + y
    if case('-'):
        print x - y
    if case('*'):
        print x * y
        break
    if case('/'):
        print x / y
        break
    if case():                      # Ĭ�Ϸ�֧
        print ""