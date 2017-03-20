#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class MyFrame(wx.Frame): #自定义窗体	
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, 'Hello World', size=(300, 300))

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)
        
        txt = wx.StaticText(panel, -1, 'Hello world!')
        sizer.Add(txt, 0, wx.TOP|wx.LEFT, 100)
        self.Centre()

class MyApp(wx.App): #自定义应用程序对象

	def OnInit(self):
		self.frame = MyFrame(None)
		self.frame.Show(True)
		return True

app = MyApp() #使用从wx.App继承的子类
app.MainLoop()