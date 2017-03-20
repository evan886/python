#!/usr/bin/python
# -*- coding: UTF-8 -*-

#导入WxPython包
import wx

class MyFrame(wx.Frame): #创建自定义Frame
	
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, 'Hello World', 
                        size=(300, 300)) #设置窗体
        
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)
        
        txt = wx.StaticText(panel, -1, 'Hello world!') #创建文本窗口部件
        sizer.Add(txt, 0, wx.TOP|wx.LEFT, 100)

        self.Centre()

app = wx.App()

frame = MyFrame(None)
frame.Show(True)

app.MainLoop() #进入事件循环