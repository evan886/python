#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class ChoiceFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'下拉列表框', size=(200, 100))
        panel = wx.Panel(self, -1)
        colorList = [u'红', u'蓝', u'绿', u'黄', u'黑', u'紫', u'白']
        wx.StaticText(panel, -1, u"选择你喜欢的颜色:", (10, 10))
        wx.Choice(panel, -1, (120, 10), choices=colorList)            # 把colorList绑定到choice控件

if __name__ == '__main__':
    app = wx.PySimpleApp()
    ChoiceFrame().Show()
    app.MainLoop()