#!/usr/bin/python
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host="smtp.qq.com" #设置服务器
mail_user="evan886"
mail_pass="uvvnqwlcerktbejb"  # 现在一般是授权码呢

sender = 'evan886@qq.com'
receivers = ['evan886@gmail.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("python学习教程", 'utf-8')
message['To'] =  Header("这里是测试", 'utf-8')
 
subject = 'Python SMTP 邮件测试 use 126 smtp'
message['Subject'] = Header(subject, 'utf-8')
 
try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"
