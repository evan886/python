#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class MyFrame(wx.Frame): #自定义窗体	
    def __init__(self, parent):
    	print "MyFrame __init__"
        wx.Frame.__init__(self, parent, -1, 'Hello World', size=(300, 300))
#省略部分代码

class MyApp(wx.App): #自定义应用程序对象
    #def __init__(self,redirect=True, filename=None):
    #    wx.App.__init__(self, redirect,filename)

	def OnInit(self):
		print "MyApp OnInit"
		self.frame = MyFrame(None)
#省略部分代码
			
	def OnExit(self):
		print "MyApp OnExit"
		import time
		time.sleep(2)
		
if __name__ == '__main__':
	print "Main start"
	app = MyApp() #使用从wx.App继承的子类
	print "Before MainLoop"
	app.MainLoop()
	print "After MainLoop"
