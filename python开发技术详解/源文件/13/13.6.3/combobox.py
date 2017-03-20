#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class ComboBoxFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'可编辑的下拉列表', size=(180, 100))
        panel = wx.Panel(self, -1)
        colorList = [u'红', u'蓝', u'绿', u'黄', u'黑', u'紫', u'白']
        wx.StaticText(panel, -1, u"你喜欢的颜色:", (20, 20))
        # 把colorList绑定到combobox
        wx.ComboBox(panel, -1, u'红', (100, 20), wx.DefaultSize, colorList, wx.CB_DROPDOWN)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    ComboBoxFrame().Show()
    app.MainLoop()