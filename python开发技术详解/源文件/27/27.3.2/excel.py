#!/usr/bin/env python
#encoding=utf-8

from time import sleep
import win32com

def excel(name):

    #生成了一个COM对象
    ex = win32com.client.Dispatch('Excel.Application')
    wk = ex.Workbooks.Add()
    nwk = wk.ActiveSheet
    ex.Visible = True
    sleep(1)

     #对Excel内容的操作

    nwk.Cells(1,1).value = u'尊敬的%s :\n'%name
    nwk.Cells(2,1).value = u'    诚邀您参加于下周五晚六点在公司举行的晚会。'


    #保存文件
    filename = name + ".xlsx"
    wk.SaveAs(filename)

    #关闭程序
    wk.Close(False)
    ex.Application.Quit()

if __name__=='__main__':
    names = ['Alice', 'Bob', 'Eve']
    for name in names:
        excel(name)

