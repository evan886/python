#!/usr/bin/env python
# -*- coding:utf-8 -*-
''' 证明正则没问题　是sendMail func有问题'''

##is me

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = 'linuxops@126.com'  # 发件人邮箱账号
my_pass = 'evan2240'  # 发件人邮箱密码
my_user = 'evan886@gmail.com'  # 收件人邮箱账号，我这边发送给自己


def mail():
    ret = True
    try:
        msg = MIMEText('天气晴朗', 'plain', 'utf-8')
        msg['From'] = formataddr(["linuxops", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "天气预报"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.126.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


#ret = mail()

#is me

import smtplib
import urllib,urllib2
import re
 
#定义函数，发送邮件
def sendMailr(body):
    smtp_server = 'smtp.qq.com'
    from_mail = '563497988@qq.com'
     
    #密码使用授权码替代，否则会报535等认证错误
    mail_pass = 'uvvnqwlcerktbejb'
    to_mail = ['evan886@gmail.com','piestion@126.com']
    from_name = 'Weather Monitor'
    subject = 'Raining Today!'
    mail = [
        "From: %s <%s>" % (from_name, from_mail),
        "To: %s" % ','.join(to_mail),
        "Subject: %s" % subject,
        "",
        body
        ]
    msg = '\n'.join(mail)
    try:
        s = smtplib.SMTP_SSL('smtp.qq.com',465)
        s.login(from_mail, mail_pass)
        s.sendmail(from_mail, to_mail, msg)
        s.quit()
    except smtplib.SMTPException as e:
        raise e


def sendMails(body):
    smtp_server = 'smtp.qq.com'
    from_mail = '563497988@qq.com'

    # 密码使用授权码替代，否则会报535等认证错误
    mail_pass = 'uvvnqwlcerktbejb'
    to_mail = ['evan886@gmail.com', 'linuxops@126.com']
    from_name = 'Weather Monitor'
    subject = 'Sunny Today!'
    mail = [
        "From: %s <%s>" % (from_name, from_mail),
        "To: %s" % ','.join(to_mail),
        "Subject: %s" % subject,
        "",
        body
    ]
    msg = '\n'.join(mail)
    try:
        s = smtplib.SMTP_SSL('smtp.qq.com', 465)
        s.login(from_mail, mail_pass)
        s.sendmail(from_mail, to_mail, msg)
        s.quit()
    except smtplib.SMTPException as e:
        raise e

if __name__ == "__main__":
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
     
    #定位城市，广州天河区
    url='http://www.tianqi.com/tianhequ/'
    try:
        request = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(request)
        urlhtml = response.read()
     
    except Exception as e:
        raise e
     
    #抓取关键字正则表达式    
    re_page = re.compile(r'<dd class="name">.*?<h2>(.*?)</h2>.*?<dd class="week">(.*?)</dd>.*?<span>.*?<b>(.*?)</b>(.*?)</span>',re.S)
     
    items = re_page.findall(urlhtml)
    dic = {}
    dic["城市"] = items[0][0]
    dic["日期"] = items[0][1]
    dic["天气"] = items[0][2]
    dic["温度"] = items[0][3]
     
    #判断天气是否含有“雨”关键字
    if "晴" in dic["天气"]:
        sendMails("It's Sunny today. Don't  bring your umbrella!" +"\n" +"城市: " +dic["城市"] +"\n" +"日期: " +dic["日期"] +"\n" +"天气: " +dic["天气"] +"\n" +"温度: " +dic["温度"])
    if "雨" in dic["天气"]:
        #ret = mail()
        sendMailr("It's rainy today. Remember to bring your umbrella!" + "\n" + "城市: " + dic["城市"] + "\n" + "日期: " + dic[
            "日期"] + "\n" + "天气: " + dic["天气"] + "\n" + "温度: " + dic["温度"])


'''
It's rainy today. Remember to bring your umbrella!
城市: 广州天河区
日期: 2018年03月28日　星期三　戊戌年二月十二
天气: 晴
温度: 17 ~ 27℃
'''

# http://blog.51cto.com/huangzp/2072702


'''
故障处理　

evan@kalipc:~/github/python/eg$ python  weather.py 
Traceback (most recent call last):
  File "weather.py", line 90, in <module>
    sendMail("It's rainy today. Remember to bring your umbrella!" +"\n" +"城市: " +dic["城市"] +"\n" +"日期: " +dic["日期"] +"\n" +"天气: " +dic["天气"] +"\n" +"温度: " +dic["温度"])
  File "weather.py", line 63, in sendMail
    raise e
smtplib.SMTPDataError: (554, 'DT:SPM 126 smtp7,DsmowADn_+Q2B7tatPL_AA--.42125S2 1522206519,please see http://mail.163.com/help/help_spam_16.htm?ip=59.41.116.229&hostid=smtp7&time=1522206519')
evan@kalipc:~/github/python/eg$ python  weather.py 

打开url 得知　
　•554 DT:SPM 发送的邮件内容包含了未被许可的信息，或被系统识别为垃圾邮件。请检查是否有用户发送病毒或者垃圾邮件；  

最后的解决办法是换成 qq smtp 
'''
'''

https://blog.csdn.net/drdairen/article/details/51134816
https://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html
http://www.runoob.com/python/python-reg-expressions.html
https://www.ibm.com/developerworks/cn/opensource/os-cn-pythonre/index.html


'''
