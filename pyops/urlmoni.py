#-*- coding:utf-8 -*-
import urllib2
import time
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_add(s):
    name, add = parseaddr(s)
    return formataddr(( \
        Header(name,'utf-8').encode(), \                        
        addr.encode("utf-8") if isinstance(addr,unicode) else addr))     

from_addr = ""
to_add = ""
password = ""
smtp_server = ""

def format_msg(s):
    #type : (object) ->object
    msg = MIMEText(s,_subtype='html',_charset='utf-8')
    msg['From'] = _format_add(from_addr)
    msg['To'] = _format_add(to_addr)
    msg['Subject'] = Header(u'来自evan的监控','utf-8').encode()
    return msg.as_string()


def send_email(s):
    
    server=

list_of_sites = []




