#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, u"简单工具栏和状态栏", size=(300, 200))
#省略部分代码
        self.CreateStatusBar()
        self.SetStatusText(u"状态栏信息")
#省略部分代码

app = wx.App()
frame = MyFrame(None)
frame.Show(True)
app.MainLoop()