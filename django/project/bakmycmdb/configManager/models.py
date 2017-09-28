#coding: utf-8
from django.db import models

# Create your models here.
CONFIG_TYPE = ((1, u'系统配置'), (2, u'应用配置'),(3, u'个性系统配置'), (4, u'个性应用配置'))

class config(models.Model):
    config_name = models.CharField(max_length=50, verbose_name=u'配置名称')
    config_type = models.IntegerField(choices=CONFIG_TYPE, verbose_name=u'所属配置类型')
    config_dir = models.CharField(max_length=255, verbose_name=u'配置路径')
    availabity = models.BigIntegerField(default=1, verbose_name=u'是否可用')

    def __unicode__(self):
        return self.config_name

    def natural_key(self):
    	return self.config_name

    class Meta:
    	db_table = 'config'
        unique_together = (('config_name', 'availabity'),)