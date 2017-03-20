#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx
import wx.html as html

class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, u"简单HTML浏览器")
        htmlwin  = html.HtmlWindow(self)

        htmlwin .LoadPage("http://www.google.com")

app = wx.PySimpleApp()
frame = MyFrame(None)
frame.Show()
app.MainLoop()