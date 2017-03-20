#!/usr/bin/python
#-*- coding:utf-8 -*-
import  logging
import os
import urllib
import time
def logs(message):
  logspath = '/data/logs/php/'
  if os.path.exists(logspath) is False:
    os.makedirs(logspath)
  logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename=logspath+'checkphp-fpm.log',
    filemode='a')
  return logging.info(message)

if __name__ == '__main__':
    message="try 3 time"
    logs(message)

'''
cat php/checkphp-fpm.log
Thu, 12 Jan 2017 15:58:00 py.py[line:14] INFO try 3 time

'''