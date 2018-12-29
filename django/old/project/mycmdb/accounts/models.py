#!/usr/bin/env python2.7
#coding: utf-8
"""
============================================================================
Author: yonghuo.x
LastChange: 2017-03-25
History:
============================================================================
"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators

from menuAuth.models import menu
# Create your models here.

class department(models.Model):
    departmentName = models.CharField(max_length=64,verbose_name=u'部门名称')
    description = models.TextField(blank=True,null=True,verbose_name=u'介绍')
    auth = models.ManyToManyField(menu, blank=True)
    availabity = models.BigIntegerField(default=1,verbose_name=u'是否可用')

    def __unicode__(self):
        return self.departmentName

    class Meta:
       db_table = 'department'
       unique_together = (('departmentName','availabity'),)

class myUser(AbstractUser):
    wechat = models.CharField(max_length=50,blank=True,null=True,verbose_name=u'微信')
    mobile = models.CharField(max_length=20,blank=True,null=True,verbose_name=u'手机',
                    validators=[validators.RegexValidator(r'^[0-9+()-]+$',
                                            ('请输入有效的手机号码。'),
                                               'invalid')])
    qq = models.CharField(max_length=50,blank=True,null=True,verbose_name=u'QQ')
    department = models.ForeignKey(department,null=True,verbose_name=u'部门')
    auth = models.ManyToManyField(menu,blank=True)
    availabity = models.BigIntegerField(default=0)

    class Meta:
       db_table = 'myUser'
       unique_together = (('username','availabity'),)