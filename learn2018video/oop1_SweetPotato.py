#!/usr/bin/python
#-*- coding:utf-8 -*-
class  SweetPotato:
    """ """
    def __init__(self):
        self.cookedString = "生的"
        self.cookedLevel = 0
        self.condiments = []

    def __str__(self):
        """ 不然打印出来是类的内存地址"""
        return "地瓜的状态:(%s)(%d),添加的作料有:(%s)" %(self.cookedString,self.cookedLevel,str(self.condiments))
  #        return "地瓜的状态:(%s)(%d),添加的作料有:(%s)" %(self.cookedString,self.cookedLevel,str(self.condiments))

    def cook(self,cooked_time):

        self.cookedLevel +=cooked_time #属性 存放你想要保存的东西  
        
        if self.cookedLevel >=0 and self.cookedLevel<3:
            self.cookedString ="生的"
        elif self.cookedLevel >=3 and self.cookedLevel<5:
            self.cookedString ="半成不熟"
        elif self.cookedLevel >=5 and self.cookedLevel<8:
            self.cookedString ="熟"
        elif self.cookedLevel >=8:
            self.cookedString ="糊了"            

            
    def addCondiments(self,item):
        self.condiments.append(item)
    

di_gua = SweetPotato()
print(di_gua)

di_gua.cook(1)
print(di_gua)

di_gua.cook(1)
print(di_gua)

di_gua.addCondiments("大蒜")
di_gua.cook(1)
print(di_gua)

di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)

di_gua.cook(1)
print(di_gua)

di_gua.cook(1)
print(di_gua)

"""
cooked_time 没有保存起来时 会这样 
地瓜的状态:(生的)(0)
地瓜的状态:(生的)(0)

  if cooked_time >=0 and cooked_time<3:
16            self.cookedString ="生的" 换成self.cookedLevel


地瓜的状态:(生的)(0),添加的作料有:([])
地瓜的状态:(生的)(1),添加的作料有:([])
地瓜的状态:(生的)(2),添加的作料有:([])
地瓜的状态:(半成不熟)(3),添加的作料有:(['大蒜'])
地瓜的状态:(半成不熟)(4),添加的作料有:(['大蒜'])
地瓜的状态:(熟)(5),添加的作料有:(['大蒜'])
地瓜的状态:(熟)(6),添加的作料有:(['大蒜'])
地瓜的状态:(熟)(7),添加的作料有:(['大蒜'])
地瓜的状态:(糊了)(8),添加的作料有:(['大蒜'])

"""
