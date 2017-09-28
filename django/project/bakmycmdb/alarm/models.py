#coding: utf-8
#author: yonghuo.x
#since: 2017-04-10

from django.db import models
from accounts.models import myUser
# Create your models here.
levelChoices = ((1,'DEBUG(1)'),(2,'INFO(2)'),(3,'WARN(3)'),(4,'FATAL(4)'))

class alarm(models.Model):
    group = models.CharField(max_length=50, verbose_name=u'组')
    name = models.CharField(max_length=50, verbose_name=u'名称')
    level = models.IntegerField(choices=levelChoices, verbose_name=u'级别')
    way = models.CharField(max_length=100, verbose_name=u'报警途径')
    user = models.ManyToManyField(myUser,verbose_name=u'接收用户')
    availabity = models.BigIntegerField(default=1, verbose_name=u'是否可用')

    class Meta:
        db_table = 'alarm'
        unique_together = (('group','level','availabity'),)

    def __unicode__(self):
        return self.name