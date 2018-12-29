#coding: utf-8
from django.db import models

# Create your models here.
'''菜单栏'''
class menu(models.Model):
    name = models.CharField(max_length=10,verbose_name=u'名称')
    htmlID = models.CharField(max_length=30)
    fatherID = models.IntegerField(default=0,verbose_name=u'上级ID')
    icon = models.CharField(max_length=30,null=True,blank=True,verbose_name=u'小图标')
    htmlClass = models.CharField(max_length=50,null=True,blank=True,verbose_name=u'样式')
    url = models.CharField(max_length=200,verbose_name=u'链接')
    availabity = models.BigIntegerField(default=1)
    class Meta:
        db_table = 'menu'
        unique_together = (('htmlID','availabity'),)