#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Singleton(object):
    __instance = None                       # ����ʵ��

    def __init__(self):
        pass

    def __new__(cls, *args, **kwd):         # ��__init__֮ǰ����
        if Singleton.__instance is None:    # ����Ψһʵ��
            Singleton.__instance = object.__new__(cls, *args, **kwd)
        return Singleton.__instance


