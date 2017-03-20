#!/usr/bin/env python
#encoding=utf-8

from time import sleep
import win32com

def word(name):

    #生成了一个COM对象
    word = win32com.client.Dispatch('Word.Application')
    doc = word.Documents.Add()
    word.Visible = True
    sleep(1)

     #对Word内容的操作
    rng = doc.Range(0,0)
    rng.InsertAfter(u'尊敬的%s :\n'%name)
    rng.InsertAfter(u'    诚邀您参加于下周五晚六点在公司举行的晚会。')
    sleep(1)

    #保存文件
    filename = name + ".doc"
    doc.SaveAs(filename)

    #关闭程序
    doc.Close(False)
    word.Application.Quit()
    print "xxxxx"

if __name__=='__main__':
    names = ['Alice', 'Bob', 'Eve']
    for name in names:
        word(name)

