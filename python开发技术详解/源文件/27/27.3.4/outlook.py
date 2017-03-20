#!/usr/bin/env python
#encoding=utf-8

from time import sleep
import win32com

def outlook(name):

    #生成了一个COM对象
    outlook = win32com.client.Dispatch('Outlook.Application')
    mail = outlook.createItem(0)
    mail.Recipients.Add('%s@server.com'%name)
	mail.Subject = u"邀请函"
	body = ""u'尊敬的%s \n'%name
	body.append(u'    诚邀您参加于下周五晚六点在公司举行的晚会。')
	mail.Body = body
	mail.Send() #发送邮件

    outlook.Quit()

if __name__=='__main__':
    names = ['Alice', 'Bob', 'Eve']
    for name in names:
        outlook(name)

