#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.
#自己定义的类
class Employee(models.Model):
    name = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.name 
