#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class CheckBoxFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'多选框', size=(120, 180))
        panel = wx.Panel(self, -1)
        wx.StaticText(panel, -1, u"你喜欢的水果：", (10, 10), (100, 20))
        wx.CheckBox(panel, -1, u"苹果", (10, 30), (100, 20))
        wx.CheckBox(panel, -1, u"香蕉", (10, 50), (100, 20))
        wx.CheckBox(panel, -1, u"西瓜", (10, 70), (100, 20))
        wx.CheckBox(panel, -1, u"桔子", (10, 90), (100, 20))

if __name__ == '__main__':
    app = wx.PySimpleApp()
    CheckBoxFrame().Show()
    app.MainLoop()