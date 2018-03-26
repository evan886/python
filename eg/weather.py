#!/usr/bin/env python
# -*- coding:utf-8 -*- 
import smtplib
import urllib,urllib2
import re
 
#定义函数，发送邮件
def sendMail(body):
    smtp_server = 'smtp.126.com'
    from_mail = 'linuxops@126.com'
     
    #密码使用授权码替代，否则会报535等认证错误
    mail_pass = 'linuxops'
    to_mail = ['evan886@qq.com']
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
        s = smtplib.SMTP_SSL('smtp.126.com',465)
        s.login(from_mail, mail_pass)
        s.sendmail(from_mail, to_mail, msg)
        s.quit()
    except smtplib.SMTPException as e:
        raise e
         
if __name__ == "__main__":
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
     
    #定位城市，深圳
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
    if "雨" in dic["天气"]:
        sendMail("It's rainy today. Remember to bring your umbrella!" +"\n" +"城市: " +dic["城市"] +"\n" +"日期: " +dic["日期"] +"\n" +"天气: " +dic["天气"] +"\n" +"温度: " +dic["温度"])
# http://blog.51cto.com/huangzp/2072702
