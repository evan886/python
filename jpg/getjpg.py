#!/usr/bin/pyton
#-*- coding:utf-8 -*-
import re
import urllib
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    #reg = r'src="(.*?\.jpg)"  width' #视频中最终用这个，但是我试了不行
    #reg=r"src=" .+\.jpg" width "

    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.jpg'  % x)
        x+=1

#html = getHtml("http://tieba.baidu.com/p/2460150866")
#https://tieba.baidu.com/p/2460150866
html = getHtml("https://tieba.baidu.com/p/3920117676")
print getImg(html)


#参考如下 一开始出不来是各种空格问题呀
# http://www.cnblogs.com/qscqesze/p/4225374.html
