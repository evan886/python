#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class MyMiniFrame(wx.MiniFrame):
    def __init__(self):
        wx.MiniFrame.__init__(self, None, -1, u'不能最小化和最大化的窗口', pos=(100, 100), size=(300, 200),
                              style=wx.DEFAULT_FRAME_STYLE | wx.CLOSE_BOX)
        # 或者sytel = wx.DEFAULT_FRAME_STYLE ^ (wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX))
        panel = wx.Panel(self, -1, size=(300, 200))

class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'自定义窗口', size=(300, 100))
        mini = MyMiniFrame()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()