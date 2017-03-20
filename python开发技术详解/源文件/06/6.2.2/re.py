#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

s = "hello world"
print re.sub("hello", "hi", s)                         
print re.sub("hello", "hi", s[-4:]) 
print re.sub("world", "China", s[-5:]) 

# ^与$的使用
s = "HELLO WORLD"
print re.findall(r"^hello", s)  
print re.findall(r"^hello", s, re.IGNORECASE)  
print re.findall("WORLD$", s)
print re.findall(r"wORld$", s, re.I)
print re.findall(r"\b\w+\b", s)  

# 特殊字符的使用
s = "你好 WORLD2"
print "匹配字母数字：" + re.sub(r"\w", "hi", s)
print "替换次数：" + str(re.subn(r"\w", "hi", s)[1])
print "匹配非字母数字的字符：" + re.sub(r"\W", "hi", s) 
print "替换次数：" + str(re.subn(r"\W", "hi", s)[1])
print "匹配空白字符：" + re.sub(r"\s", "*", s)  
print "替换次数：" + str(re.subn(r"\s", "*", s)[1])
print "匹配非空白字符：" + re.sub(r"\S", "hi", s) 
print "替换次数：" + str(re.subn(r"\S", "hi", s) [1])
print "匹配数字：" + re.sub(r"\d", "2.0", s)
print "替换次数：" + str(re.subn(r"\d", "2.0", s)[1])
print "匹配非数字：" + re.sub(r"\D", "hi", s) 
print "替换次数：" + str(re.subn(r"\D", "hi", s)[1])
print "匹配任意字符：" + re.sub(r".", "hi", s)  
print "替换次数：" + str(re.subn(r".", "hi", s)[1])

# 限定符的使用
tel1 = "0791-1234567"
print re.findall(r"\d{3}-\d{8}|\d{4}-\d{7}", tel1)
tel2 = "010-12345678"
print re.findall(r"\d{3}-\d{8}|\d{4}-\d{7}", tel2)
tel3 = "(010)12345678"
print re.findall(r"[\(]?\d{3}[\)-]?\d{8}|[\(]?\d{4}[\)-]?\d{7}", tel3)
print re.findall(r"a.*?c", "abcabc")

# compile()预编译
s = "1abc23def45"
p = re.compile(r"\d+")
print p.findall(s)
print p.pattern 

# 分组
p = re.compile(r"(abc)\1")
m = p.match("abcabcabc")
print m.group(0)
print m.group(1)
print m.group()

p = re.compile(r"(?P<one>abc)(?P=one)")
m = p.search("abcabcabc")
print m.group(0)
print m.group("one")
print m.groupdict().keys()
print m.groupdict().values()


