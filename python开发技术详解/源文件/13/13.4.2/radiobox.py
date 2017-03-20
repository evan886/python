#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class RadioBoxFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'单选框', size=(320, 150))
        panel = wx.Panel(self, -1)
        colorList = [u'红', u'蓝', u'绿', u'黄', u'黑', u'紫', u'白']
        # 生成RadioBox
        wx.RadioBox(panel, -1, u'颜色', (10, 10), wx.DefaultSize, colorList, 4, wx.RA_SPECIFY_COLS)
        wx.RadioBox(panel, -1, u'颜色', (180, 10), wx.DefaultSize, colorList, 3, wx.RA_SPECIFY_ROWS)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    RadioBoxFrame().Show()
    app.MainLoop()