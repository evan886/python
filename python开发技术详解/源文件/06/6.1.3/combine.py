#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ʹ��"+"�����ַ���
str1 = "hello "
str2 = "world "
str3 = "hello "
str4 = "China "
result = str1 + str2 + str3
result += str4
print result

# ʹ��join()�����ַ���
strs = ["hello ", "world ", "hello ", "China "]
result = "".join(strs)
print result

# ʹ��reduce()�����ַ���
import operator
strs = ["hello ", "world ", "hello ", "China "]
result = reduce(operator.add, strs, "")
print result

