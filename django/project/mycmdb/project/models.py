#coding: utf-8
from django.db import models

# Create your models here.
class appRole(models.Model):
    #app_name = models.ForeignKey(app, verbose_name=u'所属应用')
    name = models.CharField(max_length=30, verbose_name=u'角色名称')
    availabity = models.BigIntegerField(default=1, verbose_name=u'是否可用')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'appRole'
        unique_together = (('name', 'availabity'),)

class app(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'应用名称')
    another_name = models.CharField(max_length=30, blank=True, null=True, verbose_name=u'别名')
    architecture = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'架构图')
    roles = models.ManyToManyField(appRole, blank=True, verbose_name=u'角色', through='app_roles')
    availabity = models.BigIntegerField(default=1, verbose_name=u'是否可用')
    
    def __unicode__(self):
        return self.name

    def natural_key(self):
        return self.name

    class Meta:
        db_table = 'app'
        unique_together = (('name', 'another_name', 'availabity'),)

class app_roles(models.Model):
    appid = models.ForeignKey(app)
    roleid = models.ForeignKey(appRole)

    def __unicode__(self):
        return "%s -> %s" % (self.appid.name,self.roleid.name)

    def natural_key(self):
        return "%s -> %s" % (self.appid.name,self.roleid.name)

    class Meta:
        db_table = 'app_roles'