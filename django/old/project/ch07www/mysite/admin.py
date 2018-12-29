#-*_ coding:utf-8 -*-
from django.contrib import admin

from mysite import models

class ProductAdmin(admin.ModelAdmin):
    list_display = ('pmodel', 'nickname','price','year')
    search_fields = ('nickname',)
    #ordering = ('price',) #从小到大
    ordering = ('-price',)  # 从大到小

admin.site.register(models.Product,ProductAdmin)

admin.site.register(models.Maker)
admin.site.register(models.PModel)

admin.site.register(models.PPhoto)
