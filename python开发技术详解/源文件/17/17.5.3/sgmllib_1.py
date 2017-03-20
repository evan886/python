#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sgmllib
import urllib

class LinkDemo(sgmllib.SGMLParser):#从SGMLParser类中继承
    def __init__(self): #构造函数
        sgmllib.SGMLParser.__init__(self)
        self.links = [] #初始化时设置links为空

    def start_a(self, attributes): #处理<a>标签
        for link in attributes:
            tag, attr = link[:2]
            if tag == "href": #当取得了URL的时候将其加入到links中
                self.links.append(attr)

f = urllib.urlopen("http://www.baidu.com") #打开指定的URL地址
data = f.read()
f.close()

ld = LinkDemo() #实例化一个LinkDemo对象
ld.feed(data)

for i,link in enumerate(ld.links): #打印相关的信息
	print i,"==>",link