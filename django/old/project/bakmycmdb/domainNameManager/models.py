#coding: utf-8

from django.db import models

# Create your models here.
class domainName(models.Model):
    name = models.CharField(max_length=20, verbose_name='域名')
    nameDistributor = models.CharField(max_length=50,verbose_name='域名供应商')
    exptresDate = models.CharField(max_length=20, verbose_name='到期时间')
    user = models.CharField(max_length=50, verbose_name='注册用户')
    email = models.CharField(max_length=50, verbose_name='注册邮箱')
    organization = models.CharField(max_length=50, verbose_name='注册公司')
    availabity = models.BigIntegerField(default=1, verbose_name='是否可用')

    def __unicode__(self):
       return self.name

    def natural_key(self):
        return self.name

    class Meta:
        db_table = 'domainName'
        unique_together = (('name', 'availabity'),)