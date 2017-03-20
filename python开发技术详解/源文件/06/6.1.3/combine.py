#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 使用"+"连接字符串
str1 = "hello "
str2 = "world "
str3 = "hello "
str4 = "China "
result = str1 + str2 + str3
result += str4
print result

# 使用join()连接字符串
strs = ["hello ", "world ", "hello ", "China "]
result = "".join(strs)
print result

# 使用reduce()连接字符串
import operator
strs = ["hello ", "world ", "hello ", "China "]
result = reduce(operator.add, strs, "")
print result

