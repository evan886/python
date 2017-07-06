#!/usr/bin/pyton
#-*- coding:utf-8 -*-
import re
import urllib
def getHtml(url):
    page=urllib.urlopen(url)
    html = page.read()
    return  html

def getImg(html):
    #reg=r"src=" .+\.jpg" width "
    reg=r'src="(.*?\.jpg)"  width '
    imgre= re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist

#print getHtml("https://tieba.baidu.com/p/3920117676")

html = getHtml("https://tieba.baidu.com/p/3920117676")
print getImg(html)

#19