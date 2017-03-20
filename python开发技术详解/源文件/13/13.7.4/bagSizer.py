#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class BagSizerFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u"布局管理器-bagSizer", size = (350, 120))
        panel = wx.Panel(self, -1)
        sizer = wx.GridBagSizer(hgap=5, vgap=5)

        colorList = [u'红', u'蓝', u'绿']
        #sizer = wx.FlexGridSizer(rows = 3, cols=3, hgap=5, vgap=5)
        #btn = []
        col = 0
        for color in colorList:
            #btn.append(wx.Button(panel, -1, color))
            btn = wx.Button(panel, -1, color)
            sizer.Add(btn, pos=(0, col))
            col = col + 1
        btn = wx.Button(panel, -1, u'紫')
        # 新的控件占用了布局管理器中已有控件的位置，将编译出错
        sizer.Add(btn, pos=(1, 0), span=(1, 3), flag=wx.EXPAND)
        btn = wx.Button(panel, -1, u'白')
        sizer.Add(btn, pos=(0, col + 1), span=(2, 1), flag=wx.EXPAND)
        btn = wx.Button(panel, -1, u'黄')
        sizer.Add(btn, pos=(2, 0), span=(1, 2), flag=wx.EXPAND)
        btn = wx.Button(panel, -1, u'黑')
        sizer.Add(btn, pos=(2, 2), span=(1, 1), flag=wx.EXPAND)
        panel.SetSizer(sizer)
        panel.Fit()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = BagSizerFrame()
    frame.Show()
    app.MainLoop()