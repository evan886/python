#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

class BitmapButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'位图按钮', size=(200, 150))
        panel = wx.Panel(self, -1)
        bmp = wx.Image("button.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.button = wx.BitmapButton(panel, -1, bmp, pos=(20, 20), size=(120, 60))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetDefault()

    def OnClick(self, event):
        wx.MessageBox("Hello world!", u"提示")

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = BitmapButtonFrame()
    frame.Show()
    app.MainLoop()