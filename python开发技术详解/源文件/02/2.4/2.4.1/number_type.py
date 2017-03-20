#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 下面的两个i并不是同一个对象
i = 1
print id(i)
i = 2
print id(i)

# 整型
i = 1
print type(i)
# 长整型
l = 9999999990
print type(l)
# 浮点型
f = 1.2
print type(f)
# 布尔型
b = True
print type(b)
# 复数类型
c = 7 + 8j
print type(c)
