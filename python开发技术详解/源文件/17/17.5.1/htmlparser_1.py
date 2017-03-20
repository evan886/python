#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
import urlparse
import HTMLParser
 
class CheckHTML(HTMLParser.HTMLParser): #从HTMLParser类中继承
    available = True
    def handle_data(self, data): #定义处理数据的方法
        if "404 Not Found" in data or "Error 404" in data: #当含有特定字符串的时候
            self.available = False

check_urls = ["index","test","help","news", "faq","download"] #需要检查的URL

for url in check_urls:
	new_url = urlparse.urljoin("http://www.python.org/",url) #拼合URL
	fp = urllib.urlopen(new_url) #打开URL资源
	data = fp.read() #读取URL资源
	fp.close()
	
	p = CheckHTML() #生成一个CheckHTML类对象
	p.feed(data) #解析上面获得的数据
	p.close()
	
	#判断URL是否存在
	if p.available:
		print new_url, "==> OK"
	else:
		print new_url, "==> Not Found"

