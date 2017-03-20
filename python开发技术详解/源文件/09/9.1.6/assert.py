#!/usr/bin/python
# -*- coding: UTF-8 -*-

# assert判断逻辑表达式
t = ("hello",)
assert len(t) >= 1
#t = ("hello")
#assert len(t) == 1

# 带message的assert语句
month = 13
assert 1 <= month <= 12, "month errors"
#assert month >= 1 and month <= 12, "month errors"