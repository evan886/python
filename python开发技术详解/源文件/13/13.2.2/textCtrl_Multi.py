#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'多行文本框', size=(250, 150))
        panel = wx.Panel(self, -1)
        # 创建多行文本框
        multiText = wx.TextCtrl(panel, -1,
               "Python is a good language."
               "wxPython is a GUI API."
               "good job!",
               pos = (10, 10), size = (180, 80), style=wx.TE_MULTILINE|wx.TE_CENTER)
        multiText.SetBackgroundColour("red")
        multiText.SetFocus()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = TextFrame()
    frame.Show()
    app.MainLoop()