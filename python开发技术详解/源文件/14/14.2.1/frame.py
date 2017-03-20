#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'自定义窗口', size=(300, 100))

if __name__ == '__main__':
    app = wx.PySimpleApp()
    myFrame = MyFrame()
    myFrame.Show()
    app.MainLoop()