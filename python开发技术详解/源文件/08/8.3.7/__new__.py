#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Singleton(object):
    __instance = None                       # 定义实例

    def __init__(self):
        pass

    def __new__(cls, *args, **kwd):         # 在__init__之前调用
        if Singleton.__instance is None:    # 生成唯一实例
            Singleton.__instance = object.__new__(cls, *args, **kwd)
        return Singleton.__instance


