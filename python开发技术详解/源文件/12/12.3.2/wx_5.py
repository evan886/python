#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, u"简单工具栏", size=(300, 200))

        toolbar = self.CreateToolBar()
        toolbar.AddLabelTool(wx.ID_EXIT, '', wx.Bitmap('./exit.png'))        
        toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.OnExit, id=wx.ID_EXIT)

        self.Centre()

    def OnExit(self, event):
        self.Close()

app = wx.App()
frame = MyFrame(None)
frame.Show(True)
app.MainLoop()
