#!/usr/bin/python
# -*- coding: UTF-8 -*-

import htmllib
import urllib
import formatter
import string

class LinkDemo(htmllib.HTMLParser): #从HTMLParser类中继承

    def __init__(self, verbose=0): #初始化的时候调用，将links设置为空。这里的links为字典结构
        self.links = {}
        f = formatter.NullFormatter()
        htmllib.HTMLParser.__init__(self, f, verbose)

    def anchor_bgn(self, href, name, type): #锚点标签开始的时候处理
        self.save_bgn()
        self.link = href

    def anchor_end(self): #锚点标签结束的时候处理
        text = string.strip(self.save_end())
        if self.link and text:
            self.links[text] = self.links.get(text, []) + [self.link]

fp = urllib.urlopen("http://www.baidu.com") #打开指定的URL
data = fp.read()
fp.close()

linkdemo = LinkDemo() #实例化一个LinkDemo对象
linkdemo.feed(data) #处理输入
linkdemo.close()

for href, link in linkdemo.links.items(): #打印相关的信息
    print href, "=>", link
