#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 下面的两个i并不是同一个对象
i = 1
print id(i)
i = 2
print id(i)
# 正确的变量命名
var_1 = 1
print var_1
_var1 = 2
print _var1
# 错误的变量命名
1_var = 3
print 1_var
$var = 4
print $var