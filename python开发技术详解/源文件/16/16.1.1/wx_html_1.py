#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx
import wx.html as html

class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, u"简单HTML窗口")
        htmlwin = html.HtmlWindow(self)

        htmlwin.SetPage(u"""<h1>一级标题</h1>
        				<b>这是HTML加粗文本</b>
        				<br></br>
        				<i>这是HTML斜体文本</i>""")

app = wx.PySimpleApp()
frame = MyFrame(None)
frame.Show()
app.MainLoop()