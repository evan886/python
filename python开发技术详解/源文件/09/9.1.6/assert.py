#!/usr/bin/python
# -*- coding: UTF-8 -*-

# assert�ж��߼����ʽ
t = ("hello",)
assert len(t) >= 1
#t = ("hello")
#assert len(t) == 1

# ��message��assert���
month = 13
assert 1 <= month <= 12, "month errors"
#assert month >= 1 and month <= 12, "month errors"