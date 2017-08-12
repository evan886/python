#!/usr/bin/python
#-*- coding:utf-8 -*-
class Ball:
    def setName(self,name):
        self.name = name
    def kick(self):
#        print("%s"  % self.name)
#        pass
        print("我叫%s,该死的谁踢我'''" % self.name)

a = Ball()
a.setName=('球a')
a.name
#b = Ball()
#b.setName=('球b')
#c = Ball()
#c.setName=('土豆')
a.kick()
#pass
