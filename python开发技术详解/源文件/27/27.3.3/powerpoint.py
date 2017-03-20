#!/usr/bin/env python
#encoding=utf-8

from time import sleep
import win32com

def powerpoint(name):

    #生成了一个COM对象
    ppt = win32com.client.Dispatch('PowerPoint.Application')
    pres = ppt.Presentations.Add()
    ppt.Visible = True
    sleep(1)

    #对Powerpoint内容的操作
    s1 = pres.Slides.Add(1,1)
    s1_0 = s1.Shapes[0].TextFrame.TextRange
    s1_0.Text = u'尊敬的%s \n'%name

    s1_1 = s1.Shapes[1].TextFrame.TextRange
    s1_1.InsertAfter(u'    诚邀您参加于下周五晚六点在公司举行的晚会。')


    #保存文件
    filename = name + ".pptx"
    pres.SaveAs(filename)

    #关闭程序
    pres.Close()
    ppt.Application.Quit()

if __name__=='__main__':
    names = ['Alice', 'Bob', 'Eve']
    for name in names:
        powerpoint(name)

