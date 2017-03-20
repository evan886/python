#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class GridSizerFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u"布局管理器-GridSizer", size = (300, 150))
        panel = wx.Panel(self, -1)
        sizer = wx.GridSizer(rows=3, cols=3, hgap=5, vgap=5)
        colorList = [u'红', u'蓝', u'绿', u'黄', u'黑', u'紫', u'白']
        for color in colorList:
            btn = wx.Button(panel, -1, color)
            sizer.Add(btn, 0, 0)
        panel.SetSizer(sizer)
        panel.Fit()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = GridSizerFrame()
    frame.Show()
    app.MainLoop()