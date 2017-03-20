#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
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

sys.modules[__name__] = "switch_class"
