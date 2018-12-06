#!/usr/bin/python
#-*- coding:utf-8 -*-
class  SweetPotato:
    """ """
    def __init__(self):
        self.cookedString = "生的"
        self.cookedLevel = 0

    def __str__(self):
        """ 不然打印出来是类的内存地址"""
        return "地瓜的状态:(%s)(%d)" %(self.cookedString,self.cookedLevel)
#        return "地瓜的状态:(%s)(%d),添加的作料有:(%s)" %(self.cookedString,self.cookedLevel,str(self.condiments))

    def cook(self,cooked_time):
        if cooked_time >=0 and cooked_time<3:
            self.cookedString ="生的"
        elif cooked_time >=3 and cooked_time<5:
            self.cookedString ="半成不熟"
        elif cooked_time >=5 and cooked_time<8:
            self.cookedString ="熟"
        elif cooked_time >=8:
            self.cookedString ="糊了"            
        


di_gua = SweetPotato()
print(di_gua)

di_gua.cook(1)
print(di_gua)
