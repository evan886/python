# coding: utf-8
from django.db import models
from project.models import app,appRole,app_roles
from configManager.models import config

#ASSET_TYPE = ((u'云服务器', u'云服务器'), (u'云数据库', u'云数据库'), (u'云缓存Redis', u'云缓存Redis'))
ASSET_TYPE = ((u'云服务器', u'云服务器'), (u'云数据库mysql', u'云数据库mysql'), (u'云缓存Redis', u'云缓存Redis'))

class dataCenter(models.Model):
    account_number = models.CharField(max_length=32, verbose_name=u'主账号')
    name = models.CharField(max_length=100, verbose_name=u'名称')
    area = models.CharField(max_length=100, verbose_name=u'区域')
    editor = models.TextField(blank=True, null=True, verbose_name=u'备注')
    availabity = models.BigIntegerField(default=1, verbose_name=u'是否可用')

    def __unicode__(self):
        return '%s -> %s' % (self.name, self.area)

    def natural_key(self):
        return '%s -> %s' % (self.name, self.area)

    class Meta:
        db_table = 'dataCenter'
        unique_together = (('name', 'area','availabity'),)

class asset(models.Model):
    group = models.ForeignKey(dataCenter, verbose_name=u'所属数据中心')
    server_type = models.CharField(max_length=30, choices=ASSET_TYPE, verbose_name=u'设备类型')
    ip = models.CharField(max_length=32, verbose_name=u'公网IP')
    #ip = models.CharField(max_length=32, verbose_name=u'管理IP')
    intraip = models.CharField(max_length=32, verbose_name=u'内网IP')
    other_ip = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'其他IP')
    port = models.IntegerField(default=22, verbose_name=u'端口号')
    is_monitoring = models.BooleanField(default=True, verbose_name=u'是否监控')
    is_backup = models.BooleanField(default=True, verbose_name=u'是否备份')
    config = models.ManyToManyField(config, blank=True, verbose_name=u'系统配置')
    app_name = models.ManyToManyField(app, blank=True,verbose_name=u'关联应用')
    role_name = models.ManyToManyField(app_roles, blank=True, verbose_name=u'应用角色名称')
    editor = models.TextField(blank=True, null=True, verbose_name=u'备注')
    availabity = models.BigIntegerField(default=1, verbose_name=u'是否可用')

    def __unicode__(self):
        return self.ip

    class Meta:
        db_table = 'asset'
        unique_together = (('ip', 'availabity'),)
