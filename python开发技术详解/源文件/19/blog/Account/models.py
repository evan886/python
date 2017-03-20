#encoding=utf-8

from django.db import models

class Account(models.Model):
    name = models.CharField('用户名', max_length=30)
    password = models.CharField('密码', max_length=30)
    email = models.EmailField('电子邮箱', blank=True)
    desc = models.TextField('描述', max_length=500, blank=True)

    def __str__(self):
        return '%s' % (self.name)