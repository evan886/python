#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
class switch(object):
    def __init__(self, value):      # 初始化需要匹配的值value
        self.value = value
        self.fall = False           # 如果匹配到的case语句中没有break，则fall为true。

    def __iter__(self):
        yield self.match            # 调用match方法 返回一个生成器
        raise StopIteration         # StopIteration 异常来判断for循环是否结束

    def match(self, *args):         # 模拟case子句的方法
        if self.fall or not args:   # 如果fall为true，则继续执行下面的case子句
                                    # 或case子句没有匹配项，则流转到默认分支。
            return True
        elif self.value in args:    # 匹配成功
            self.fall = True
            return True
        else:                       # 匹配失败
            return False

sys.modules[__name__] = "switch_class"
