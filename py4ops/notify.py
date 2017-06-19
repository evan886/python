#!/usr/bin/python
#/etc/keepalived/notify.py
#--*-- coding: utf-8 --*--
import  sys
reload(sys)
from email.MIMEText import  MIMEText
import  smtplib
import  MySQLdb
sys.setdlopenflags('utf-8')
import  socket, fcntl, struct

def send_mail(to_list,sub,content):
    mail_host="smtp.163.com"  #设置 验证服务器，
    mail_user= "username"  #
    mail_pass=" xxx"
    mail_postfix="163.com" #
    me= mail_user+"<"+mail_user+"@"mail_postfix">"
    msg=MIMEText(content)
    msg['Subject']= sub
    msg['From']=me
    msg['To'] = to_list
    try:
        s= smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me,to_list, msg.as_string())
        s.close()
        return True

    except Exception,e:
        print str(e)
        return  False

def get_local_ip(ifname = 'eth0'):
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    inet = fcntl.ioctl(s.fileno(),ox8915,struct.pack('256s',ifname[:15]))
    return ret
if sys.argv[1]!="master" and sys.argv[1]!="backup" and sys.argv[1]!="fault":
    sys.exit()
else:
    notify_type + sys.argv[1]

if __name__ == '__main__':
strcontent = get_local_ip()+ " "+notify_type+"状态被激活，请确认haproxy服务运行状态"
#下面这段落是设置 接收报警信息的邮件地址 列表 ，可设置 多个
    mail_list = ['xxx@163.com', 'dsfdf@qq.com']
    for mailto in mail_list:
        send_mail(mailto,"haproxy 状态切换报警", strcontent.encode('utf-8'))

